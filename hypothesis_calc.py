# ============================================================================
# CALCULADORA ESTATÍSTICA INTERATIVA PARA TESTES DE HIPÓTESE
# ============================================================================
# Implementação modular de fórmulas para testes de hipótese
# Sem interpretação: apenas métricas calculadas
# ============================================================================

import numpy as np
from scipy import stats
from typing import Dict, List, Tuple, Optional


# ============================================================================
# FUNÇÕES AUXILIARES
# ============================================================================

def parse_sample_input(sample_input: str) -> List[float]:
    """
    Converte string de entrada em lista de valores numéricos.
    Exemplo: "10 12 9 11 13" -> [10, 12, 9, 11, 13]
    """
    try:
        return [float(x.strip()) for x in sample_input.split() if x.strip()]
    except ValueError:
        raise ValueError("Erro: Valores inválidos. Use números separados por espaço.")


def calculate_sample_stats(sample: List[float]) -> Tuple[float, float, float, int]:
    """
    Calcula média, variância (S²), desvio padrão (S) e tamanho da amostra.
    
    Retorna: (média, S², S, n)
    """
    n = len(sample)
    if n < 2:
        raise ValueError("Erro: Amostra deve ter pelo menos 2 elementos.")
    
    mean = sum(sample) / n
    # Variância amostral com divisor (n-1)
    variance = sum((x - mean) ** 2 for x in sample) / (n - 1)
    std_dev = np.sqrt(variance)
    
    return mean, variance, std_dev, n


def validate_alpha(alpha: float) -> None:
    """Valida se alpha está entre 0 e 1."""
    if not (0 < alpha < 1):
        raise ValueError("Erro: α deve estar entre 0 e 1.")


def validate_sample_size(n: int) -> None:
    """Valida se n >= 2."""
    if n < 2:
        raise ValueError("Erro: Tamanho da amostra deve ser >= 2.")


def get_input_mode() -> str:
    """Permite escolher entre entrada direta ou amostra completa."""
    print("\n[1] Inserir valores resumidos (x̄, S, n)")
    print("[2] Inserir amostra completa")
    choice = input("Escolha [1/2]: ").strip()
    return choice


def get_test_type() -> str:
    """Menu para escolher o tipo de teste."""
    print("\n" + "="*70)
    print("TIPOS DE TESTES DISPONÍVEIS")
    print("="*70)
    print("[1] Média com variância desconhecida (Teste t)")
    print("[2] Diferença entre médias (variâncias desconhecidas e iguais)")
    print("[3] Diferença entre médias (variâncias desconhecidas e diferentes - Welch)")
    print("[4] Amostras emparelhadas (Teste t pareado)")
    print("[5] Média com variância conhecida (Teste Z)")
    print("[6] Proporção (Teste Z)")
    print("[7] Variância (Teste Chi-quadrado)")
    print("[8] Diferença entre proporções (Teste Z)")
    print("[9] Diferença entre variâncias (Teste F)")
    
    choice = input("\nEscolha o teste [1-9]: ").strip()
    return choice


# ============================================================================
# TESTE 1: MÉDIA COM VARIÂNCIA DESCONHECIDA (TESTE T)
# ============================================================================

def test_mean_unknown_variance(
    x_bar: Optional[float] = None,
    s: Optional[float] = None,
    n: Optional[int] = None,
    mu_0: Optional[float] = None,
    alpha: Optional[float] = None,
    sample: Optional[List[float]] = None
) -> Dict[str, float]:
    """
    Teste t para média com variância desconhecida.
    
    Fórmula: T = (x̄ - μ₀) / (S / √n)
    Distribuição: t com (n-1) graus de liberdade
    """
    
    # Se amostra completa for fornecida, calcular estatísticas
    if sample is not None:
        x_bar, _, s, n = calculate_sample_stats(sample)
    
    # Validar entrada
    if any(v is None for v in [x_bar, s, n, mu_0, alpha]):
        raise ValueError("Erro: Valores incompletos para o teste.")
    
    validate_alpha(alpha)
    validate_sample_size(n)
    
    # Calcular estatística de teste
    t_calc = (x_bar - mu_0) / (s / np.sqrt(n))
    
    # Graus de liberdade
    df = n - 1
    
    # Valores críticos (bilateral, unilateral direita, unilateral esquerda)
    t_crit_bilateral = stats.t.ppf(1 - alpha/2, df)
    t_crit_unilateral = stats.t.ppf(1 - alpha, df)
    
    return {
        "x_bar": round(x_bar, 2),
        "s": round(s, 2),
        "n": n,
        "mu_0": mu_0,
        "alpha": alpha,
        "t_calc": round(t_calc, 2),
        "df": df,
        "t_critico_bilateral": round(t_crit_bilateral, 2),
        "t_critico_unilateral": round(t_crit_unilateral, 2)
    }


# ============================================================================
# TESTE 2: DIFERENÇA ENTRE MÉDIAS (VARIÂNCIAS DESCONHECIDAS E IGUAIS)
# ============================================================================

def test_diff_means_equal_variances(
    x_bar_1: Optional[float] = None,
    x_bar_2: Optional[float] = None,
    s_sq_1: Optional[float] = None,
    s_sq_2: Optional[float] = None,
    n_1: Optional[int] = None,
    n_2: Optional[int] = None,
    alpha: Optional[float] = None,
    sample_1: Optional[List[float]] = None,
    sample_2: Optional[List[float]] = None
) -> Dict[str, float]:
    """
    Teste t para diferença entre médias com variâncias desconhecidas e iguais.
    
    Fórmula:
    - S²_p = [(n₁-1)S₁² + (n₂-1)S₂²] / (n₁ + n₂ - 2)
    - T = (x̄₁ - x̄₂) / (S_p * √(1/n₁ + 1/n₂))
    - Distribuição: t com (n₁ + n₂ - 2) graus de liberdade
    """
    
    # Se amostras completas forem fornecidas, calcular estatísticas
    if sample_1 is not None and sample_2 is not None:
        x_bar_1, s_sq_1, _, n_1 = calculate_sample_stats(sample_1)
        x_bar_2, s_sq_2, _, n_2 = calculate_sample_stats(sample_2)
    
    # Validar entrada
    if any(v is None for v in [x_bar_1, x_bar_2, s_sq_1, s_sq_2, n_1, n_2, alpha]):
        raise ValueError("Erro: Valores incompletos para o teste.")
    
    validate_alpha(alpha)
    validate_sample_size(n_1)
    validate_sample_size(n_2)
    
    # Calcular variância pooled (agrupada)
    s_p_sq = ((n_1 - 1) * s_sq_1 + (n_2 - 1) * s_sq_2) / (n_1 + n_2 - 2)
    s_p = np.sqrt(s_p_sq)
    
    # Calcular estatística de teste
    t_calc = (x_bar_1 - x_bar_2) / (s_p * np.sqrt(1/n_1 + 1/n_2))
    
    # Graus de liberdade
    df = n_1 + n_2 - 2
    
    # Valores críticos
    t_crit_bilateral = stats.t.ppf(1 - alpha/2, df)
    t_crit_unilateral = stats.t.ppf(1 - alpha, df)
    
    return {
        "x_bar_1": round(x_bar_1, 2),
        "x_bar_2": round(x_bar_2, 2),
        "s_sq_1": round(s_sq_1, 2),
        "s_sq_2": round(s_sq_2, 2),
        "n_1": n_1,
        "n_2": n_2,
        "alpha": alpha,
        "s_p_sq": round(s_p_sq, 2),
        "s_p": round(s_p, 2),
        "t_calc": round(t_calc, 2),
        "df": df,
        "t_critico_bilateral": round(t_crit_bilateral, 2),
        "t_critico_unilateral": round(t_crit_unilateral, 2)
    }


# ============================================================================
# TESTE 3: DIFERENÇA ENTRE MÉDIAS (VARIÂNCIAS DESCONHECIDAS E DIFERENTES - WELCH)
# ============================================================================

def test_diff_means_welch(
    x_bar_1: Optional[float] = None,
    x_bar_2: Optional[float] = None,
    s_sq_1: Optional[float] = None,
    s_sq_2: Optional[float] = None,
    n_1: Optional[int] = None,
    n_2: Optional[int] = None,
    alpha: Optional[float] = None,
    sample_1: Optional[List[float]] = None,
    sample_2: Optional[List[float]] = None
) -> Dict[str, float]:
    """
    Teste t de Welch para diferença entre médias com variâncias desconhecidas e diferentes.
    
    Fórmula:
    - W_i = S²_i / n_i
    - T = (x̄₁ - x̄₂) / √(W₁ + W₂)
    - ν ≈ (W₁ + W₂)² / [(W₁²)/(n₁+1) + (W₂²)/(n₂+1)]
    - Distribuição: t com ν graus de liberdade
    """
    
    # Se amostras completas forem fornecidas
    if sample_1 is not None and sample_2 is not None:
        x_bar_1, s_sq_1, _, n_1 = calculate_sample_stats(sample_1)
        x_bar_2, s_sq_2, _, n_2 = calculate_sample_stats(sample_2)
    
    # Validar entrada
    if any(v is None for v in [x_bar_1, x_bar_2, s_sq_1, s_sq_2, n_1, n_2, alpha]):
        raise ValueError("Erro: Valores incompletos para o teste.")
    
    validate_alpha(alpha)
    validate_sample_size(n_1)
    validate_sample_size(n_2)
    
    # Calcular W_i
    w_1 = s_sq_1 / n_1
    w_2 = s_sq_2 / n_2
    
    # Calcular estatística de teste
    t_calc = (x_bar_1 - x_bar_2) / np.sqrt(w_1 + w_2)
    
    # Calcular graus de liberdade (Welch-Satterthwaite)
    numerator = (w_1 + w_2) ** 2
    denominator = (w_1 ** 2) / (n_1 + 1) + (w_2 ** 2) / (n_2 + 1)
    df = numerator / denominator
    
    # Valores críticos
    t_crit_bilateral = stats.t.ppf(1 - alpha/2, df)
    t_crit_unilateral = stats.t.ppf(1 - alpha, df)
    
    return {
        "x_bar_1": round(x_bar_1, 2),
        "x_bar_2": round(x_bar_2, 2),
        "s_sq_1": round(s_sq_1, 2),
        "s_sq_2": round(s_sq_2, 2),
        "n_1": n_1,
        "n_2": n_2,
        "alpha": alpha,
        "w_1": round(w_1, 2),
        "w_2": round(w_2, 2),
        "t_calc": round(t_calc, 2),
        "df": round(df, 2),
        "t_critico_bilateral": round(t_crit_bilateral, 2),
        "t_critico_unilateral": round(t_crit_unilateral, 2)
    }


# ============================================================================
# TESTE 4: AMOSTRAS EMPARELHADAS (TESTE T PAREADO)
# ============================================================================

def test_paired_samples(
    d_bar: Optional[float] = None,
    s_d: Optional[float] = None,
    n: Optional[int] = None,
    delta: float = 0,
    alpha: Optional[float] = None,
    sample_diff: Optional[List[float]] = None
) -> Dict[str, float]:
    """
    Teste t para amostras emparelhadas.
    
    Fórmula: T = (d̄ - Δ) / (S_d / √n)
    Onde d̄ é a média das diferenças e S_d é o desvio padrão
    Distribuição: t com (n-1) graus de liberdade
    """
    
    # Se amostra de diferenças for fornecida
    if sample_diff is not None:
        d_bar, _, s_d, n = calculate_sample_stats(sample_diff)
    
    # Validar entrada
    if any(v is None for v in [d_bar, s_d, n, alpha]):
        raise ValueError("Erro: Valores incompletos para o teste.")
    
    validate_alpha(alpha)
    validate_sample_size(n)
    
    # Calcular estatística de teste
    t_calc = (d_bar - delta) / (s_d / np.sqrt(n))
    
    # Graus de liberdade
    df = n - 1
    
    # Valores críticos
    t_crit_bilateral = stats.t.ppf(1 - alpha/2, df)
    t_crit_unilateral = stats.t.ppf(1 - alpha, df)
    
    return {
        "d_bar": round(d_bar, 2),
        "s_d": round(s_d, 2),
        "n": n,
        "delta": delta,
        "alpha": alpha,
        "t_calc": round(t_calc, 2),
        "df": df,
        "t_critico_bilateral": round(t_crit_bilateral, 2),
        "t_critico_unilateral": round(t_crit_unilateral, 2)
    }


# ============================================================================
# TESTE 5: MÉDIA COM VARIÂNCIA CONHECIDA (TESTE Z)
# ============================================================================

def test_mean_known_variance(
    x_bar: Optional[float] = None,
    sigma: Optional[float] = None,
    n: Optional[int] = None,
    mu_0: Optional[float] = None,
    alpha: Optional[float] = None,
    sample: Optional[List[float]] = None
) -> Dict[str, float]:
    """
    Teste Z para média com variância conhecida.
    
    Fórmula: Z = (x̄ - μ₀) / (σ / √n)
    Distribuição: Normal padrão N(0,1)
    """
    
    # Se amostra completa for fornecida (apenas para calcular média e n)
    if sample is not None:
        x_bar = sum(sample) / len(sample)
        n = len(sample)
    
    # Validar entrada
    if any(v is None for v in [x_bar, sigma, n, mu_0, alpha]):
        raise ValueError("Erro: Valores incompletos para o teste.")
    
    validate_alpha(alpha)
    validate_sample_size(n)
    
    # Calcular estatística de teste
    z_calc = (x_bar - mu_0) / (sigma / np.sqrt(n))
    
    # Valores críticos
    z_crit_bilateral = stats.norm.ppf(1 - alpha/2)
    z_crit_unilateral = stats.norm.ppf(1 - alpha)
    
    return {
        "x_bar": round(x_bar, 2),
        "sigma": sigma,
        "n": n,
        "mu_0": mu_0,
        "alpha": alpha,
        "z_calc": round(z_calc, 2),
        "z_critico_bilateral": round(z_crit_bilateral, 2),
        "z_critico_unilateral": round(z_crit_unilateral, 2)
    }


# ============================================================================
# TESTE 6: PROPORÇÃO (TESTE Z)
# ============================================================================

def test_proportion(
    p_hat: Optional[float] = None,
    p_0: Optional[float] = None,
    n: Optional[int] = None,
    alpha: Optional[float] = None,
    successes: Optional[int] = None
) -> Dict[str, float]:
    """
    Teste Z para proporção.
    
    Fórmula: Z = (p̂ - p₀) / √[p₀(1-p₀)/n]
    Distribuição: Normal padrão N(0,1)
    
    Se successes for fornecido: p̂ = successes / n
    """
    
    # Se número de sucessos for fornecido
    if successes is not None and n is not None:
        p_hat = successes / n
    
    # Validar entrada
    if any(v is None for v in [p_hat, p_0, n, alpha]):
        raise ValueError("Erro: Valores incompletos para o teste.")
    
    validate_alpha(alpha)
    validate_sample_size(n)
    
    if not (0 <= p_hat <= 1 and 0 <= p_0 <= 1):
        raise ValueError("Erro: Proporções devem estar entre 0 e 1.")
    
    # Calcular estatística de teste
    z_calc = (p_hat - p_0) / np.sqrt(p_0 * (1 - p_0) / n)
    
    # Valores críticos
    z_crit_bilateral = stats.norm.ppf(1 - alpha/2)
    z_crit_unilateral = stats.norm.ppf(1 - alpha)
    
    return {
        "p_hat": round(p_hat, 2),
        "p_0": p_0,
        "n": n,
        "alpha": alpha,
        "z_calc": round(z_calc, 2),
        "z_critico_bilateral": round(z_crit_bilateral, 2),
        "z_critico_unilateral": round(z_crit_unilateral, 2)
    }


# ============================================================================
# TESTE 7: VARIÂNCIA (TESTE CHI-QUADRADO)
# ============================================================================

def test_variance(
    s_sq: Optional[float] = None,
    sigma_0_sq: Optional[float] = None,
    n: Optional[int] = None,
    alpha: Optional[float] = None,
    sample: Optional[List[float]] = None
) -> Dict[str, float]:
    """
    Teste Chi-quadrado para variância.
    
    Fórmula: χ² = (n-1)S² / σ₀²
    Distribuição: Chi-quadrado com (n-1) graus de liberdade
    """
    
    # Se amostra completa for fornecida
    if sample is not None:
        _, s_sq, _, n = calculate_sample_stats(sample)
    
    # Validar entrada
    if any(v is None for v in [s_sq, sigma_0_sq, n, alpha]):
        raise ValueError("Erro: Valores incompletos para o teste.")
    
    validate_alpha(alpha)
    validate_sample_size(n)
    
    if sigma_0_sq <= 0:
        raise ValueError("Erro: σ₀² deve ser positivo.")
    
    # Calcular estatística de teste
    chi_sq_calc = (n - 1) * s_sq / sigma_0_sq
    
    # Graus de liberdade
    df = n - 1
    
    # Valores críticos (bilateral)
    chi_sq_crit_lower = stats.chi2.ppf(alpha/2, df)
    chi_sq_crit_upper = stats.chi2.ppf(1 - alpha/2, df)
    
    # Unilateral direita e esquerda
    chi_sq_crit_upper_uni = stats.chi2.ppf(1 - alpha, df)
    chi_sq_crit_lower_uni = stats.chi2.ppf(alpha, df)
    
    return {
        "s_sq": round(s_sq, 2),
        "sigma_0_sq": sigma_0_sq,
        "n": n,
        "alpha": alpha,
        "chi_sq_calc": round(chi_sq_calc, 2),
        "df": df,
        "chi_sq_critico_bilateral_lower": round(chi_sq_crit_lower, 2),
        "chi_sq_critico_bilateral_upper": round(chi_sq_crit_upper, 2),
        "chi_sq_critico_unilateral_dir": round(chi_sq_crit_upper_uni, 2),
        "chi_sq_critico_unilateral_esq": round(chi_sq_crit_lower_uni, 2)
    }


# ============================================================================
# TESTE 8: DIFERENÇA ENTRE PROPORÇÕES (TESTE Z)
# ============================================================================

def test_diff_proportions(
    p_hat_1: Optional[float] = None,
    p_hat_2: Optional[float] = None,
    n_1: Optional[int] = None,
    n_2: Optional[int] = None,
    alpha: Optional[float] = None,
    successes_1: Optional[int] = None,
    successes_2: Optional[int] = None
) -> Dict[str, float]:
    """
    Teste Z para diferença entre proporções.
    
    Fórmula:
    - p̂ = (f₁ + f₂) / (n₁ + n₂)
    - Z = (p̂₁ - p̂₂) / √[p̂(1-p̂)(1/n₁ + 1/n₂)]
    Distribuição: Normal padrão N(0,1)
    """
    
    # Se números de sucessos forem fornecidos
    if successes_1 is not None and successes_2 is not None:
        p_hat_1 = successes_1 / n_1
        p_hat_2 = successes_2 / n_2
    
    # Validar entrada
    if any(v is None for v in [p_hat_1, p_hat_2, n_1, n_2, alpha]):
        raise ValueError("Erro: Valores incompletos para o teste.")
    
    validate_alpha(alpha)
    validate_sample_size(n_1)
    validate_sample_size(n_2)
    
    if not (0 <= p_hat_1 <= 1 and 0 <= p_hat_2 <= 1):
        raise ValueError("Erro: Proporções devem estar entre 0 e 1.")
    
    # Calcular proporção pooled
    p_hat = (p_hat_1 * n_1 + p_hat_2 * n_2) / (n_1 + n_2)
    
    # Calcular estatística de teste
    z_calc = (p_hat_1 - p_hat_2) / np.sqrt(p_hat * (1 - p_hat) * (1/n_1 + 1/n_2))
    
    # Valores críticos
    z_crit_bilateral = stats.norm.ppf(1 - alpha/2)
    z_crit_unilateral = stats.norm.ppf(1 - alpha)
    
    return {
        "p_hat_1": round(p_hat_1, 2),
        "p_hat_2": round(p_hat_2, 2),
        "n_1": n_1,
        "n_2": n_2,
        "alpha": alpha,
        "p_hat_pooled": round(p_hat, 2),
        "z_calc": round(z_calc, 2),
        "z_critico_bilateral": round(z_crit_bilateral, 2),
        "z_critico_unilateral": round(z_crit_unilateral, 2)
    }


# ============================================================================
# TESTE 9: DIFERENÇA ENTRE VARIÂNCIAS (TESTE F)
# ============================================================================

def test_diff_variances(
    s_sq_1: Optional[float] = None,
    s_sq_2: Optional[float] = None,
    n_1: Optional[int] = None,
    n_2: Optional[int] = None,
    alpha: Optional[float] = None,
    sample_1: Optional[List[float]] = None,
    sample_2: Optional[List[float]] = None
) -> Dict[str, float]:
    """
    Teste F para diferença entre variâncias.
    
    Fórmula: F = S₁² / S₂² (ou razão da maior pela menor para bilateral)
    Distribuição: F com (n₁-1, n₂-1) graus de liberdade
    """
    
    # Se amostras completas forem fornecidas
    if sample_1 is not None and sample_2 is not None:
        _, s_sq_1, _, n_1 = calculate_sample_stats(sample_1)
        _, s_sq_2, _, n_2 = calculate_sample_stats(sample_2)
    
    # Validar entrada
    if any(v is None for v in [s_sq_1, s_sq_2, n_1, n_2, alpha]):
        raise ValueError("Erro: Valores incompletos para o teste.")
    
    validate_alpha(alpha)
    validate_sample_size(n_1)
    validate_sample_size(n_2)
    
    # Calcular estatística de teste (S₁² / S₂²)
    f_calc = s_sq_1 / s_sq_2
    
    # Graus de liberdade
    df_1 = n_1 - 1
    df_2 = n_2 - 1
    
    # Valores críticos
    f_crit_bilateral = stats.f.ppf(1 - alpha/2, df_1, df_2)
    f_crit_unilateral = stats.f.ppf(1 - alpha, df_1, df_2)
    
    return {
        "s_sq_1": round(s_sq_1, 2),
        "s_sq_2": round(s_sq_2, 2),
        "n_1": n_1,
        "n_2": n_2,
        "alpha": alpha,
        "f_calc": round(f_calc, 2),
        "df_1": df_1,
        "df_2": df_2,
        "f_critico_bilateral": round(f_crit_bilateral, 2),
        "f_critico_unilateral": round(f_crit_unilateral, 2)
    }


# ============================================================================
# INTERFACE INTERATIVA
# ============================================================================

def run_interactive_calculator():
    """Menu interativo principal."""
    
    while True:
        try:
            test_choice = get_test_type()
            
            if test_choice == "1":
                # Teste 1: Média com variância desconhecida
                print("\n--- Teste de Média com Variância Desconhecida ---")
                input_mode = get_input_mode()
                
                if input_mode == "1":
                    x_bar = float(input("x̄ (média amostral): "))
                    s = float(input("S (desvio padrão amostral): "))
                    n = int(input("n (tamanho da amostra): "))
                    mu_0 = float(input("μ₀ (média sob H₀): "))
                    alpha = float(input("α (nível de significância): "))
                    
                    result = test_mean_unknown_variance(
                        x_bar=x_bar, s=s, n=n, mu_0=mu_0, alpha=alpha
                    )
                else:
                    sample_str = input("Digite os valores da amostra (separados por espaço): ")
                    sample = parse_sample_input(sample_str)
                    mu_0 = float(input("μ₀ (média sob H₀): "))
                    alpha = float(input("α (nível de significância): "))
                    
                    result = test_mean_unknown_variance(
                        mu_0=mu_0, alpha=alpha, sample=sample
                    )
                
                print("\n--- RESULTADOS ---")
                for key, value in result.items():
                    print(f"{key}: {value}")
            
            elif test_choice == "2":
                # Teste 2: Diferença entre médias (variâncias iguais)
                print("\n--- Teste de Diferença entre Médias (Variâncias Iguais) ---")
                input_mode = get_input_mode()
                
                if input_mode == "1":
                    x_bar_1 = float(input("x̄₁ (média amostra 1): "))
                    x_bar_2 = float(input("x̄₂ (média amostra 2): "))
                    s_sq_1 = float(input("S₁² (variância amostra 1): "))
                    s_sq_2 = float(input("S₂² (variância amostra 2): "))
                    n_1 = int(input("n₁ (tamanho amostra 1): "))
                    n_2 = int(input("n₂ (tamanho amostra 2): "))
                    alpha = float(input("α (nível de significância): "))
                    
                    result = test_diff_means_equal_variances(
                        x_bar_1=x_bar_1, x_bar_2=x_bar_2,
                        s_sq_1=s_sq_1, s_sq_2=s_sq_2,
                        n_1=n_1, n_2=n_2, alpha=alpha
                    )
                else:
                    sample_1_str = input("Digite os valores da amostra 1: ")
                    sample_1 = parse_sample_input(sample_1_str)
                    sample_2_str = input("Digite os valores da amostra 2: ")
                    sample_2 = parse_sample_input(sample_2_str)
                    alpha = float(input("α (nível de significância): "))
                    
                    result = test_diff_means_equal_variances(
                        alpha=alpha, sample_1=sample_1, sample_2=sample_2
                    )
                
                print("\n--- RESULTADOS ---")
                for key, value in result.items():
                    print(f"{key}: {value}")
            
            elif test_choice == "3":
                # Teste 3: Welch
                print("\n--- Teste de Welch (Variâncias Diferentes) ---")
                input_mode = get_input_mode()
                
                if input_mode == "1":
                    x_bar_1 = float(input("x̄₁ (média amostra 1): "))
                    x_bar_2 = float(input("x̄₂ (média amostra 2): "))
                    s_sq_1 = float(input("S₁² (variância amostra 1): "))
                    s_sq_2 = float(input("S₂² (variância amostra 2): "))
                    n_1 = int(input("n₁ (tamanho amostra 1): "))
                    n_2 = int(input("n₂ (tamanho amostra 2): "))
                    alpha = float(input("α (nível de significância): "))
                    
                    result = test_diff_means_welch(
                        x_bar_1=x_bar_1, x_bar_2=x_bar_2,
                        s_sq_1=s_sq_1, s_sq_2=s_sq_2,
                        n_1=n_1, n_2=n_2, alpha=alpha
                    )
                else:
                    sample_1_str = input("Digite os valores da amostra 1: ")
                    sample_1 = parse_sample_input(sample_1_str)
                    sample_2_str = input("Digite os valores da amostra 2: ")
                    sample_2 = parse_sample_input(sample_2_str)
                    alpha = float(input("α (nível de significância): "))
                    
                    result = test_diff_means_welch(
                        alpha=alpha, sample_1=sample_1, sample_2=sample_2
                    )
                
                print("\n--- RESULTADOS ---")
                for key, value in result.items():
                    print(f"{key}: {value}")
            
            elif test_choice == "4":
                # Teste 4: Amostras pareadas
                print("\n--- Teste de Amostras Pareadas ---")
                input_mode = get_input_mode()
                
                if input_mode == "1":
                    d_bar = float(input("d̄ (média das diferenças): "))
                    s_d = float(input("S_d (desvio padrão das diferenças): "))
                    n = int(input("n (número de pares): "))
                    delta = float(input("Δ (valor sob H₀) [padrão 0]: ") or "0")
                    alpha = float(input("α (nível de significância): "))
                    
                    result = test_paired_samples(
                        d_bar=d_bar, s_d=s_d, n=n, delta=delta, alpha=alpha
                    )
                else:
                    diff_str = input("Digite as diferenças (separadas por espaço): ")
                    sample_diff = parse_sample_input(diff_str)
                    delta = float(input("Δ (valor sob H₀) [padrão 0]: ") or "0")
                    alpha = float(input("α (nível de significância): "))
                    
                    result = test_paired_samples(
                        delta=delta, alpha=alpha, sample_diff=sample_diff
                    )
                
                print("\n--- RESULTADOS ---")
                for key, value in result.items():
                    print(f"{key}: {value}")
            
            elif test_choice == "5":
                # Teste 5: Média com variância conhecida
                print("\n--- Teste Z para Média com Variância Conhecida ---")
                input_mode = get_input_mode()
                
                if input_mode == "1":
                    x_bar = float(input("x̄ (média amostral): "))
                    sigma = float(input("σ (desvio padrão populacional): "))
                    n = int(input("n (tamanho da amostra): "))
                    mu_0 = float(input("μ₀ (média sob H₀): "))
                    alpha = float(input("α (nível de significância): "))
                    
                    result = test_mean_known_variance(
                        x_bar=x_bar, sigma=sigma, n=n, mu_0=mu_0, alpha=alpha
                    )
                else:
                    sample_str = input("Digite os valores da amostra: ")
                    sample = parse_sample_input(sample_str)
                    sigma = float(input("σ (desvio padrão populacional): "))
                    mu_0 = float(input("μ₀ (média sob H₀): "))
                    alpha = float(input("α (nível de significância): "))
                    
                    result = test_mean_known_variance(
                        sigma=sigma, mu_0=mu_0, alpha=alpha, sample=sample
                    )
                
                print("\n--- RESULTADOS ---")
                for key, value in result.items():
                    print(f"{key}: {value}")
            
            elif test_choice == "6":
                # Teste 6: Proporção
                print("\n--- Teste Z para Proporção ---")
                choice_prop = input("Inserir p̂ diretamente [1] ou número de sucessos [2]? ").strip()
                
                if choice_prop == "1":
                    p_hat = float(input("p̂ (proporção amostral): "))
                else:
                    successes = int(input("Número de sucessos: "))
                    n = int(input("n (tamanho da amostra): "))
                    p_hat = successes / n
                
                n = int(input("n (tamanho da amostra): ")) if choice_prop == "1" else n
                p_0 = float(input("p₀ (proporção sob H₀): "))
                alpha = float(input("α (nível de significância): "))
                
                result = test_proportion(
                    p_hat=p_hat, p_0=p_0, n=n, alpha=alpha
                )
                
                print("\n--- RESULTADOS ---")
                for key, value in result.items():
                    print(f"{key}: {value}")
            
            elif test_choice == "7":
                # Teste 7: Variância
                print("\n--- Teste Chi-quadrado para Variância ---")
                input_mode = get_input_mode()
                
                if input_mode == "1":
                    s_sq = float(input("S² (variância amostral): "))
                    sigma_0_sq = float(input("σ₀² (variância sob H₀): "))
                    n = int(input("n (tamanho da amostra): "))
                    alpha = float(input("α (nível de significância): "))
                    
                    result = test_variance(
                        s_sq=s_sq, sigma_0_sq=sigma_0_sq, n=n, alpha=alpha
                    )
                else:
                    sample_str = input("Digite os valores da amostra: ")
                    sample = parse_sample_input(sample_str)
                    sigma_0_sq = float(input("σ₀² (variância sob H₀): "))
                    alpha = float(input("α (nível de significância): "))
                    
                    result = test_variance(
                        sigma_0_sq=sigma_0_sq, alpha=alpha, sample=sample
                    )
                
                print("\n--- RESULTADOS ---")
                for key, value in result.items():
                    print(f"{key}: {value}")
            
            elif test_choice == "8":
                # Teste 8: Diferença entre proporções
                print("\n--- Teste Z para Diferença entre Proporções ---")
                
                choice_prop = input("Inserir p̂ diretamente [1] ou número de sucessos [2]? ").strip()
                
                if choice_prop == "1":
                    p_hat_1 = float(input("p̂₁ (proporção amostra 1): "))
                    p_hat_2 = float(input("p̂₂ (proporção amostra 2): "))
                    n_1 = int(input("n₁ (tamanho amostra 1): "))
                    n_2 = int(input("n₂ (tamanho amostra 2): "))
                else:
                    successes_1 = int(input("Sucessos amostra 1: "))
                    n_1 = int(input("n₁ (tamanho amostra 1): "))
                    successes_2 = int(input("Sucessos amostra 2: "))
                    n_2 = int(input("n₂ (tamanho amostra 2): "))
                    p_hat_1 = None
                    p_hat_2 = None
                
                alpha = float(input("α (nível de significância): "))
                
                if choice_prop == "1":
                    result = test_diff_proportions(
                        p_hat_1=p_hat_1, p_hat_2=p_hat_2, n_1=n_1, n_2=n_2, alpha=alpha
                    )
                else:
                    result = test_diff_proportions(
                        n_1=n_1, n_2=n_2, alpha=alpha,
                        successes_1=successes_1, successes_2=successes_2
                    )
                
                print("\n--- RESULTADOS ---")
                for key, value in result.items():
                    print(f"{key}: {value}")
            
            elif test_choice == "9":
                # Teste 9: Diferença entre variâncias
                print("\n--- Teste F para Diferença entre Variâncias ---")
                input_mode = get_input_mode()
                
                if input_mode == "1":
                    s_sq_1 = float(input("S₁² (variância amostra 1): "))
                    s_sq_2 = float(input("S₂² (variância amostra 2): "))
                    n_1 = int(input("n₁ (tamanho amostra 1): "))
                    n_2 = int(input("n₂ (tamanho amostra 2): "))
                    alpha = float(input("α (nível de significância): "))
                    
                    result = test_diff_variances(
                        s_sq_1=s_sq_1, s_sq_2=s_sq_2, n_1=n_1, n_2=n_2, alpha=alpha
                    )
                else:
                    sample_1_str = input("Digite os valores da amostra 1: ")
                    sample_1 = parse_sample_input(sample_1_str)
                    sample_2_str = input("Digite os valores da amostra 2: ")
                    sample_2 = parse_sample_input(sample_2_str)
                    alpha = float(input("α (nível de significância): "))
                    
                    result = test_diff_variances(
                        alpha=alpha, sample_1=sample_1, sample_2=sample_2
                    )
                
                print("\n--- RESULTADOS ---")
                for key, value in result.items():
                    print(f"{key}: {value}")
            
            else:
                print("Opção inválida. Tente novamente.")
                continue
            
            # Menu para repetir
            repeat = input("\nDeseja fazer outro cálculo? [S/N]: ").strip().upper()
            if repeat != "S":
                print("\nEncerrando calculadora. Até logo!")
                break
        
        except ValueError as e:
            print(f"\n❌ Erro de entrada: {e}")
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")


if __name__ == "__main__":
    print("="*70)
    print("CALCULADORA ESTATÍSTICA PARA TESTES DE HIPÓTESE")
    print("="*70)
    print("Fórmulas implementadas manualmente")
    print("Sem interpretação: apenas métricas calculadas")
    print("="*70)
    
    run_interactive_calculator()
