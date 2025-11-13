"""
CALCULADORA ESTATÍSTICA INTERATIVA - TESTES DE HIPÓTESES
========================================================

Script modular para calcular métricas intermediárias de diversos tipos de testes
de hipóteses, sem interpretar resultados finais.

Utiliza: NumPy e scipy.stats (distribuições)
Proibido: pandas, statsmodels

Autor: Sistema de Análise Estatística
Data: 2025
"""

import numpy as np
from scipy import stats


# ============================================================================
# FUNÇÕES AUXILIARES E VALIDAÇÃO
# ============================================================================

def validar_entrada_numerica(valor_str, nome_var):
    """
    Valida se uma entrada é um número válido.
    
    Args:
        valor_str (str): String a ser convertida
        nome_var (str): Nome da variável (para mensagem de erro)
    
    Returns:
        float: Valor convertido
    
    Raises:
        ValueError: Se não for número válido
    """
    try:
        return float(valor_str)
    except ValueError:
        raise ValueError(f"'{nome_var}' deve ser um número válido. Recebido: {valor_str}")


def validar_parametros(n=None, alpha=None, s=None):
    """
    Valida restrições comuns em parâmetros estatísticos.
    
    Args:
        n (float): Tamanho da amostra
        alpha (float): Nível de significância
        s (float): Desvio padrão amostral
    
    Raises:
        ValueError: Se valores forem inválidos
    """
    if n is not None and n <= 1:
        raise ValueError(f"Tamanho da amostra 'n' deve ser > 1. Recebido: {n}")
    
    if alpha is not None and (alpha <= 0 or alpha >= 1):
        raise ValueError(f"Nível de significância 'α' deve estar entre 0 e 1. Recebido: {alpha}")
    
    if s is not None and s < 0:
        raise ValueError(f"Desvio padrão 'S' não pode ser negativo. Recebido: {s}")


def formatar_resultado(resultado_dict):
    """
    Formata dicionário de resultados para exibição limpa.
    
    Args:
        resultado_dict (dict): Dicionário com resultados
    
    Returns:
        str: String formatada com resultados
    """
    output = "\n" + "="*60 + "\n"
    output += "MÉTRICAS CALCULADAS\n"
    output += "="*60 + "\n"
    
    for chave, valor in resultado_dict.items():
        if isinstance(valor, float):
            output += f"{chave:.<30} {valor:.2f}\n"
        else:
            output += f"{chave:.<30} {valor}\n"
    
    output += "="*60 + "\n"
    return output


# ============================================================================
# TESTES SOBRE UMA AMOSTRA
# ============================================================================

def t_media_var_desconhecida():
    """
    Teste t para média com variância desconhecida.
    
    Fórmula: T = (X̄ - μ₀) / (S / √n)
    Distribuição: t(n-1)
    
    Entradas:
        - Média amostral (X̄)
        - Valor hipotético (μ₀)
        - Desvio padrão amostral (S)
        - Tamanho da amostra (n)
        - Nível de significância (α)
        - Tipo de teste (bilateral/unilateral_dir/unilateral_esq)
    
    Retorna:
        dict: Contendo t_calculado, t_crítico, graus de liberdade
    """
    print("\n--- TESTE T PARA MÉDIA (VARIÂNCIA DESCONHECIDA) ---")
    
    try:
        x_barra = validar_entrada_numerica(
            input("Média amostral (X̄): "),
            "X̄"
        )
        mu_0 = validar_entrada_numerica(
            input("Valor hipotético (μ₀): "),
            "μ₀"
        )
        s = validar_entrada_numerica(
            input("Desvio padrão amostral (S): "),
            "S"
        )
        n = validar_entrada_numerica(
            input("Tamanho da amostra (n): "),
            "n"
        )
        alpha = validar_entrada_numerica(
            input("Nível de significância (α): "),
            "α"
        )
        
        tipo_teste = input(
            "Tipo de teste (bilateral/unilateral_dir/unilateral_esq): "
        ).lower().strip()
        
        if tipo_teste not in ["bilateral", "unilateral_dir", "unilateral_esq"]:
            raise ValueError("Tipo de teste inválido")
        
        validar_parametros(n=n, alpha=alpha, s=s)
        
        # Cálculos
        gl = n - 1  # graus de liberdade
        t_calc = (x_barra - mu_0) / (s / np.sqrt(n))
        
        # t_crítico conforme tipo de teste
        if tipo_teste == "bilateral":
            t_crit = stats.t.ppf(1 - alpha/2, gl)
        elif tipo_teste == "unilateral_dir":
            t_crit = stats.t.ppf(1 - alpha, gl)
        else:  # unilateral_esq
            t_crit = -stats.t.ppf(1 - alpha, gl)
        
        resultado = {
            "Tipo de Teste": tipo_teste,
            "Graus de Liberdade (gl)": int(gl),
            "t_calculado": t_calc,
            "t_crítico": t_crit,
            "Nível de Significância (α)": alpha
        }
        
        return resultado
    
    except ValueError as e:
        print(f"❌ Erro na validação: {e}")
        return None


def z_media_var_conhecida():
    """
    Teste Z para média com variância conhecida.
    
    Fórmula: Z = (X̄ - μ₀) / (σ / √n)
    Distribuição: N(0,1)
    
    Entradas:
        - Média amostral (X̄)
        - Valor hipotético (μ₀)
        - Desvio padrão populacional (σ)
        - Tamanho da amostra (n)
        - Nível de significância (α)
        - Tipo de teste
    
    Retorna:
        dict: Contendo z_calculado, z_crítico
    """
    print("\n--- TESTE Z PARA MÉDIA (VARIÂNCIA CONHECIDA) ---")
    
    try:
        x_barra = validar_entrada_numerica(
            input("Média amostral (X̄): "),
            "X̄"
        )
        mu_0 = validar_entrada_numerica(
            input("Valor hipotético (μ₀): "),
            "μ₀"
        )
        sigma = validar_entrada_numerica(
            input("Desvio padrão populacional (σ): "),
            "σ"
        )
        n = validar_entrada_numerica(
            input("Tamanho da amostra (n): "),
            "n"
        )
        alpha = validar_entrada_numerica(
            input("Nível de significância (α): "),
            "α"
        )
        
        tipo_teste = input(
            "Tipo de teste (bilateral/unilateral_dir/unilateral_esq): "
        ).lower().strip()
        
        if tipo_teste not in ["bilateral", "unilateral_dir", "unilateral_esq"]:
            raise ValueError("Tipo de teste inválido")
        
        validar_parametros(n=n, alpha=alpha, s=sigma)
        
        # Cálculos
        z_calc = (x_barra - mu_0) / (sigma / np.sqrt(n))
        
        # z_crítico conforme tipo de teste
        if tipo_teste == "bilateral":
            z_crit = stats.norm.ppf(1 - alpha/2)
        elif tipo_teste == "unilateral_dir":
            z_crit = stats.norm.ppf(1 - alpha)
        else:  # unilateral_esq
            z_crit = -stats.norm.ppf(1 - alpha)
        
        resultado = {
            "Tipo de Teste": tipo_teste,
            "z_calculado": z_calc,
            "z_crítico": z_crit,
            "Nível de Significância (α)": alpha
        }
        
        return resultado
    
    except ValueError as e:
        print(f"❌ Erro na validação: {e}")
        return None


def chi2_variancia():
    """
    Teste Qui-Quadrado para variância.
    
    Fórmula: χ² = (n-1)S² / σ₀²
    Distribuição: χ²(n-1)
    
    Entradas:
        - Desvio padrão amostral (S)
        - Variância hipotética (σ₀²)
        - Tamanho da amostra (n)
        - Nível de significância (α)
        - Tipo de teste
    
    Retorna:
        dict: Contendo chi2_calculado, chi2_crítico
    """
    print("\n--- TESTE QUI-QUADRADO PARA VARIÂNCIA ---")
    
    try:
        s = validar_entrada_numerica(
            input("Desvio padrão amostral (S): "),
            "S"
        )
        sigma2_0 = validar_entrada_numerica(
            input("Variância hipotética (σ₀²): "),
            "σ₀²"
        )
        n = validar_entrada_numerica(
            input("Tamanho da amostra (n): "),
            "n"
        )
        alpha = validar_entrada_numerica(
            input("Nível de significância (α): "),
            "α"
        )
        
        tipo_teste = input(
            "Tipo de teste (bilateral/unilateral_dir/unilateral_esq): "
        ).lower().strip()
        
        if tipo_teste not in ["bilateral", "unilateral_dir", "unilateral_esq"]:
            raise ValueError("Tipo de teste inválido")
        
        validar_parametros(n=n, alpha=alpha, s=s)
        
        if sigma2_0 <= 0:
            raise ValueError("Variância hipotética deve ser positiva")
        
        # Cálculos
        gl = n - 1  # graus de liberdade
        chi2_calc = ((n - 1) * (s ** 2)) / sigma2_0
        
        # chi2_crítico conforme tipo de teste
        if tipo_teste == "bilateral":
            chi2_crit_inf = stats.chi2.ppf(alpha/2, gl)
            chi2_crit_sup = stats.chi2.ppf(1 - alpha/2, gl)
            resultado = {
                "Tipo de Teste": tipo_teste,
                "Graus de Liberdade (gl)": int(gl),
                "χ²_calculado": chi2_calc,
                "χ²_crítico (inferior)": chi2_crit_inf,
                "χ²_crítico (superior)": chi2_crit_sup,
                "Nível de Significância (α)": alpha
            }
        elif tipo_teste == "unilateral_dir":
            chi2_crit = stats.chi2.ppf(1 - alpha, gl)
            resultado = {
                "Tipo de Teste": tipo_teste,
                "Graus de Liberdade (gl)": int(gl),
                "χ²_calculado": chi2_calc,
                "χ²_crítico": chi2_crit,
                "Nível de Significância (α)": alpha
            }
        else:  # unilateral_esq
            chi2_crit = stats.chi2.ppf(alpha, gl)
            resultado = {
                "Tipo de Teste": tipo_teste,
                "Graus de Liberdade (gl)": int(gl),
                "χ²_calculado": chi2_calc,
                "χ²_crítico": chi2_crit,
                "Nível de Significância (α)": alpha
            }
        
        return resultado
    
    except ValueError as e:
        print(f"❌ Erro na validação: {e}")
        return None


def z_proporcao():
    """
    Teste Z para proporção.
    
    Fórmula: Z = (p̂ - p₀) / √(p₀(1-p₀)/n)
    Distribuição: N(0,1)
    
    Entradas:
        - Proporção amostral (p̂)
        - Proporção hipotética (p₀)
        - Tamanho da amostra (n)
        - Nível de significância (α)
        - Tipo de teste
    
    Retorna:
        dict: Contendo z_calculado, z_crítico
    """
    print("\n--- TESTE Z PARA PROPORÇÃO ---")
    
    try:
        p_hat = validar_entrada_numerica(
            input("Proporção amostral (p̂): "),
            "p̂"
        )
        p_0 = validar_entrada_numerica(
            input("Proporção hipotética (p₀): "),
            "p₀"
        )
        n = validar_entrada_numerica(
            input("Tamanho da amostra (n): "),
            "n"
        )
        alpha = validar_entrada_numerica(
            input("Nível de significância (α): "),
            "α"
        )
        
        tipo_teste = input(
            "Tipo de teste (bilateral/unilateral_dir/unilateral_esq): "
        ).lower().strip()
        
        if tipo_teste not in ["bilateral", "unilateral_dir", "unilateral_esq"]:
            raise ValueError("Tipo de teste inválido")
        
        validar_parametros(n=n, alpha=alpha)
        
        if not (0 <= p_hat <= 1) or not (0 <= p_0 <= 1):
            raise ValueError("Proporções devem estar entre 0 e 1")
        
        # Cálculos
        z_calc = (p_hat - p_0) / np.sqrt((p_0 * (1 - p_0)) / n)
        
        # z_crítico conforme tipo de teste
        if tipo_teste == "bilateral":
            z_crit = stats.norm.ppf(1 - alpha/2)
        elif tipo_teste == "unilateral_dir":
            z_crit = stats.norm.ppf(1 - alpha)
        else:  # unilateral_esq
            z_crit = -stats.norm.ppf(1 - alpha)
        
        resultado = {
            "Tipo de Teste": tipo_teste,
            "z_calculado": z_calc,
            "z_crítico": z_crit,
            "Nível de Significância (α)": alpha
        }
        
        return resultado
    
    except ValueError as e:
        print(f"❌ Erro na validação: {e}")
        return None


# ============================================================================
# TESTES SOBRE DUAS AMOSTRAS
# ============================================================================

def t_dif_medias_var_iguais():
    """
    Teste t para diferença entre médias com variâncias desconhecidas e iguais.
    
    Fórmula:
        T = (X̄₁ - X̄₂) / (Sp * √(1/n₁ + 1/n₂))
        Sp² = ((n₁-1)S₁² + (n₂-1)S₂²) / (n₁ + n₂ - 2)
    
    Distribuição: t(n₁+n₂-2)
    
    Entradas:
        - Média amostra 1 (X̄₁)
        - Média amostra 2 (X̄₂)
        - Desvio padrão amostra 1 (S₁)
        - Desvio padrão amostra 2 (S₂)
        - Tamanho amostra 1 (n₁)
        - Tamanho amostra 2 (n₂)
        - Nível de significância (α)
        - Tipo de teste
    
    Retorna:
        dict: Contendo Sp², t_calculado, t_crítico
    """
    print("\n--- TESTE T PARA DIFERENÇA ENTRE MÉDIAS (VARIÂNCIAS IGUAIS) ---")
    
    try:
        x1_barra = validar_entrada_numerica(
            input("Média amostra 1 (X̄₁): "),
            "X̄₁"
        )
        x2_barra = validar_entrada_numerica(
            input("Média amostra 2 (X̄₂): "),
            "X̄₂"
        )
        s1 = validar_entrada_numerica(
            input("Desvio padrão amostra 1 (S₁): "),
            "S₁"
        )
        s2 = validar_entrada_numerica(
            input("Desvio padrão amostra 2 (S₂): "),
            "S₂"
        )
        n1 = validar_entrada_numerica(
            input("Tamanho amostra 1 (n₁): "),
            "n₁"
        )
        n2 = validar_entrada_numerica(
            input("Tamanho amostra 2 (n₂): "),
            "n₂"
        )
        alpha = validar_entrada_numerica(
            input("Nível de significância (α): "),
            "α"
        )
        
        tipo_teste = input(
            "Tipo de teste (bilateral/unilateral_dir/unilateral_esq): "
        ).lower().strip()
        
        if tipo_teste not in ["bilateral", "unilateral_dir", "unilateral_esq"]:
            raise ValueError("Tipo de teste inválido")
        
        validar_parametros(n=n1, alpha=alpha, s=s1)
        validar_parametros(n=n2, alpha=alpha, s=s2)
        
        # Cálculos
        gl = n1 + n2 - 2  # graus de liberdade
        
        # Variância ponderada (pooled variance)
        sp2 = ((n1 - 1) * (s1 ** 2) + (n2 - 1) * (s2 ** 2)) / gl
        sp = np.sqrt(sp2)
        
        # Estatística t
        t_calc = (x1_barra - x2_barra) / (sp * np.sqrt(1/n1 + 1/n2))
        
        # t_crítico conforme tipo de teste
        if tipo_teste == "bilateral":
            t_crit = stats.t.ppf(1 - alpha/2, gl)
        elif tipo_teste == "unilateral_dir":
            t_crit = stats.t.ppf(1 - alpha, gl)
        else:  # unilateral_esq
            t_crit = -stats.t.ppf(1 - alpha, gl)
        
        resultado = {
            "Tipo de Teste": tipo_teste,
            "Graus de Liberdade (gl)": int(gl),
            "Variância Ponderada (Sp²)": sp2,
            "Desvio Padrão Ponderado (Sp)": sp,
            "t_calculado": t_calc,
            "t_crítico": t_crit,
            "Nível de Significância (α)": alpha
        }
        
        return resultado
    
    except ValueError as e:
        print(f"❌ Erro na validação: {e}")
        return None


def t_welch_dif_medias():
    """
    Teste t de Welch para diferença entre médias com variâncias desconhecidas e diferentes.
    
    Fórmula:
        T = (X̄₁ - X̄₂) / √(W₁ + W₂)
        W_i = S_i² / n_i
        ν ≈ (W₁ + W₂)² / ((W₁²/(n₁+1)) + (W₂²/(n₂+1)))
    
    Distribuição: t(ν)
    
    Retorna:
        dict: Contendo W₁, W₂, t_calculado, graus_liberdade_welch, t_crítico
    """
    print("\n--- TESTE T DE WELCH (VARIÂNCIAS DIFERENTES) ---")
    
    try:
        x1_barra = validar_entrada_numerica(
            input("Média amostra 1 (X̄₁): "),
            "X̄₁"
        )
        x2_barra = validar_entrada_numerica(
            input("Média amostra 2 (X̄₂): "),
            "X̄₂"
        )
        s1 = validar_entrada_numerica(
            input("Desvio padrão amostra 1 (S₁): "),
            "S₁"
        )
        s2 = validar_entrada_numerica(
            input("Desvio padrão amostra 2 (S₂): "),
            "S₂"
        )
        n1 = validar_entrada_numerica(
            input("Tamanho amostra 1 (n₁): "),
            "n₁"
        )
        n2 = validar_entrada_numerica(
            input("Tamanho amostra 2 (n₂): "),
            "n₂"
        )
        alpha = validar_entrada_numerica(
            input("Nível de significância (α): "),
            "α"
        )
        
        tipo_teste = input(
            "Tipo de teste (bilateral/unilateral_dir/unilateral_esq): "
        ).lower().strip()
        
        if tipo_teste not in ["bilateral", "unilateral_dir", "unilateral_esq"]:
            raise ValueError("Tipo de teste inválido")
        
        validar_parametros(n=n1, alpha=alpha, s=s1)
        validar_parametros(n=n2, alpha=alpha, s=s2)
        
        # Cálculos
        W1 = (s1 ** 2) / n1
        W2 = (s2 ** 2) / n2
        
        # Graus de liberdade de Welch
        numerador = (W1 + W2) ** 2
        denominador = (W1 ** 2) / (n1 + 1) + (W2 ** 2) / (n2 + 1)
        gl_welch = numerador / denominador
        
        # Estatística t
        t_calc = (x1_barra - x2_barra) / np.sqrt(W1 + W2)
        
        # t_crítico conforme tipo de teste
        if tipo_teste == "bilateral":
            t_crit = stats.t.ppf(1 - alpha/2, gl_welch)
        elif tipo_teste == "unilateral_dir":
            t_crit = stats.t.ppf(1 - alpha, gl_welch)
        else:  # unilateral_esq
            t_crit = -stats.t.ppf(1 - alpha, gl_welch)
        
        resultado = {
            "Tipo de Teste": tipo_teste,
            "W₁ (S₁²/n₁)": W1,
            "W₂ (S₂²/n₂)": W2,
            "Graus de Liberdade Welch (ν)": gl_welch,
            "t_calculado": t_calc,
            "t_crítico": t_crit,
            "Nível de Significância (α)": alpha
        }
        
        return resultado
    
    except ValueError as e:
        print(f"❌ Erro na validação: {e}")
        return None


def t_pareado():
    """
    Teste t pareado (amostras emparelhadas).
    
    Fórmula:
        T = (d̄ - Δ) / (Sd / √n)
        d_i = x_i - y_i (diferenças)
    
    Distribuição: t(n-1)
    
    Entradas:
        - Média das diferenças (d̄)
        - Diferença hipotética (Δ)
        - Desvio padrão das diferenças (Sd)
        - Número de pares (n)
        - Nível de significância (α)
        - Tipo de teste
    
    Retorna:
        dict: Contendo t_calculado, t_crítico
    """
    print("\n--- TESTE T PAREADO (AMOSTRAS EMPARELHADAS) ---")
    
    try:
        d_barra = validar_entrada_numerica(
            input("Média das diferenças (d̄): "),
            "d̄"
        )
        delta = validar_entrada_numerica(
            input("Diferença hipotética (Δ) [default 0]: ") or "0",
            "Δ"
        )
        sd = validar_entrada_numerica(
            input("Desvio padrão das diferenças (Sd): "),
            "Sd"
        )
        n = validar_entrada_numerica(
            input("Número de pares (n): "),
            "n"
        )
        alpha = validar_entrada_numerica(
            input("Nível de significância (α): "),
            "α"
        )
        
        tipo_teste = input(
            "Tipo de teste (bilateral/unilateral_dir/unilateral_esq): "
        ).lower().strip()
        
        if tipo_teste not in ["bilateral", "unilateral_dir", "unilateral_esq"]:
            raise ValueError("Tipo de teste inválido")
        
        validar_parametros(n=n, alpha=alpha, s=sd)
        
        # Cálculos
        gl = n - 1  # graus de liberdade
        t_calc = (d_barra - delta) / (sd / np.sqrt(n))
        
        # t_crítico conforme tipo de teste
        if tipo_teste == "bilateral":
            t_crit = stats.t.ppf(1 - alpha/2, gl)
        elif tipo_teste == "unilateral_dir":
            t_crit = stats.t.ppf(1 - alpha, gl)
        else:  # unilateral_esq
            t_crit = -stats.t.ppf(1 - alpha, gl)
        
        resultado = {
            "Tipo de Teste": tipo_teste,
            "Graus de Liberdade (gl)": int(gl),
            "Diferença Hipotética (Δ)": delta,
            "t_calculado": t_calc,
            "t_crítico": t_crit,
            "Nível de Significância (α)": alpha
        }
        
        return resultado
    
    except ValueError as e:
        print(f"❌ Erro na validação: {e}")
        return None


def z_dif_medias_var_conhecidas():
    """
    Teste Z para diferença entre médias com variâncias conhecidas.
    
    Fórmula: Z = (X̄₁ - X̄₂) / √(σ₁²/n₁ + σ₂²/n₂)
    Distribuição: N(0,1)
    
    Retorna:
        dict: Contendo z_calculado, z_crítico
    """
    print("\n--- TESTE Z PARA DIFERENÇA ENTRE MÉDIAS (VARIÂNCIAS CONHECIDAS) ---")
    
    try:
        x1_barra = validar_entrada_numerica(
            input("Média amostra 1 (X̄₁): "),
            "X̄₁"
        )
        x2_barra = validar_entrada_numerica(
            input("Média amostra 2 (X̄₂): "),
            "X̄₂"
        )
        sigma1 = validar_entrada_numerica(
            input("Desvio padrão populacional 1 (σ₁): "),
            "σ₁"
        )
        sigma2 = validar_entrada_numerica(
            input("Desvio padrão populacional 2 (σ₂): "),
            "σ₂"
        )
        n1 = validar_entrada_numerica(
            input("Tamanho amostra 1 (n₁): "),
            "n₁"
        )
        n2 = validar_entrada_numerica(
            input("Tamanho amostra 2 (n₂): "),
            "n₂"
        )
        alpha = validar_entrada_numerica(
            input("Nível de significância (α): "),
            "α"
        )
        
        tipo_teste = input(
            "Tipo de teste (bilateral/unilateral_dir/unilateral_esq): "
        ).lower().strip()
        
        if tipo_teste not in ["bilateral", "unilateral_dir", "unilateral_esq"]:
            raise ValueError("Tipo de teste inválido")
        
        validar_parametros(n=n1, alpha=alpha, s=sigma1)
        validar_parametros(n=n2, alpha=alpha, s=sigma2)
        
        # Cálculos
        z_calc = (x1_barra - x2_barra) / np.sqrt((sigma1**2)/n1 + (sigma2**2)/n2)
        
        # z_crítico conforme tipo de teste
        if tipo_teste == "bilateral":
            z_crit = stats.norm.ppf(1 - alpha/2)
        elif tipo_teste == "unilateral_dir":
            z_crit = stats.norm.ppf(1 - alpha)
        else:  # unilateral_esq
            z_crit = -stats.norm.ppf(1 - alpha)
        
        resultado = {
            "Tipo de Teste": tipo_teste,
            "z_calculado": z_calc,
            "z_crítico": z_crit,
            "Nível de Significância (α)": alpha
        }
        
        return resultado
    
    except ValueError as e:
        print(f"❌ Erro na validação: {e}")
        return None


def z_dif_proporcoes():
    """
    Teste Z para diferença entre proporções.
    
    Fórmula:
        Z = (p̂₁ - p̂₂) / √(p̂(1-p̂)(1/n₁ + 1/n₂))
        p̂ = (f₁ + f₂) / (n₁ + n₂)  [proporção combinada]
    
    Entradas:
        - Proporção amostra 1 (p̂₁)
        - Proporção amostra 2 (p̂₂)
        - Tamanho amostra 1 (n₁)
        - Tamanho amostra 2 (n₂)
        - Nível de significância (α)
        - Tipo de teste
    
    Retorna:
        dict: Contendo p̂_combinada, z_calculado, z_crítico
    """
    print("\n--- TESTE Z PARA DIFERENÇA ENTRE PROPORÇÕES ---")
    
    try:
        p1_hat = validar_entrada_numerica(
            input("Proporção amostra 1 (p̂₁): "),
            "p̂₁"
        )
        p2_hat = validar_entrada_numerica(
            input("Proporção amostra 2 (p̂₂): "),
            "p̂₂"
        )
        n1 = validar_entrada_numerica(
            input("Tamanho amostra 1 (n₁): "),
            "n₁"
        )
        n2 = validar_entrada_numerica(
            input("Tamanho amostra 2 (n₂): "),
            "n₂"
        )
        alpha = validar_entrada_numerica(
            input("Nível de significância (α): "),
            "α"
        )
        
        tipo_teste = input(
            "Tipo de teste (bilateral/unilateral_dir/unilateral_esq): "
        ).lower().strip()
        
        if tipo_teste not in ["bilateral", "unilateral_dir", "unilateral_esq"]:
            raise ValueError("Tipo de teste inválido")
        
        validar_parametros(n=n1, alpha=alpha)
        validar_parametros(n=n2, alpha=alpha)
        
        if not (0 <= p1_hat <= 1) or not (0 <= p2_hat <= 1):
            raise ValueError("Proporções devem estar entre 0 e 1")
        
        # Cálculos
        # Proporção combinada (usando contagens)
        f1 = p1_hat * n1
        f2 = p2_hat * n2
        p_combinada = (f1 + f2) / (n1 + n2)
        
        # Estatística z
        z_calc = (p1_hat - p2_hat) / np.sqrt(p_combinada * (1 - p_combinada) * (1/n1 + 1/n2))
        
        # z_crítico conforme tipo de teste
        if tipo_teste == "bilateral":
            z_crit = stats.norm.ppf(1 - alpha/2)
        elif tipo_teste == "unilateral_dir":
            z_crit = stats.norm.ppf(1 - alpha)
        else:  # unilateral_esq
            z_crit = -stats.norm.ppf(1 - alpha)
        
        resultado = {
            "Tipo de Teste": tipo_teste,
            "Proporção Combinada (p̂)": p_combinada,
            "z_calculado": z_calc,
            "z_crítico": z_crit,
            "Nível de Significância (α)": alpha
        }
        
        return resultado
    
    except ValueError as e:
        print(f"❌ Erro na validação: {e}")
        return None


def f_dif_variancias():
    """
    Teste F para diferença entre variâncias.
    
    Fórmula: F = S₁² / S₂² (ou max/min para bilateral)
    Distribuição: F(n₁-1, n₂-1)
    
    Entradas:
        - Desvio padrão amostra 1 (S₁)
        - Desvio padrão amostra 2 (S₂)
        - Tamanho amostra 1 (n₁)
        - Tamanho amostra 2 (n₂)
        - Nível de significância (α)
        - Tipo de teste
    
    Retorna:
        dict: Contendo f_calculado, f_crítico
    """
    print("\n--- TESTE F PARA DIFERENÇA ENTRE VARIÂNCIAS ---")
    
    try:
        s1 = validar_entrada_numerica(
            input("Desvio padrão amostra 1 (S₁): "),
            "S₁"
        )
        s2 = validar_entrada_numerica(
            input("Desvio padrão amostra 2 (S₂): "),
            "S₂"
        )
        n1 = validar_entrada_numerica(
            input("Tamanho amostra 1 (n₁): "),
            "n₁"
        )
        n2 = validar_entrada_numerica(
            input("Tamanho amostra 2 (n₂): "),
            "n₂"
        )
        alpha = validar_entrada_numerica(
            input("Nível de significância (α): "),
            "α"
        )
        
        tipo_teste = input(
            "Tipo de teste (bilateral/unilateral_dir): "
        ).lower().strip()
        
        if tipo_teste not in ["bilateral", "unilateral_dir"]:
            raise ValueError("Tipo de teste inválido para teste F")
        
        validar_parametros(n=n1, alpha=alpha, s=s1)
        validar_parametros(n=n2, alpha=alpha, s=s2)
        
        # Cálculos
        gl1 = n1 - 1
        gl2 = n2 - 1
        
        if tipo_teste == "bilateral":
            # Usa max/min para bilateral
            s_max = max(s1, s2)
            s_min = min(s1, s2)
            f_calc = (s_max ** 2) / (s_min ** 2)
            
            # Ajusta graus de liberdade de acordo com qual variância é maior
            if s1 > s2:
                f_crit = stats.f.ppf(1 - alpha/2, gl1, gl2)
            else:
                f_crit = stats.f.ppf(1 - alpha/2, gl2, gl1)
        else:  # unilateral_dir
            f_calc = (s1 ** 2) / (s2 ** 2)
            f_crit = stats.f.ppf(1 - alpha, gl1, gl2)
        
        resultado = {
            "Tipo de Teste": tipo_teste,
            "Graus de Liberdade 1 (gl1)": int(gl1),
            "Graus de Liberdade 2 (gl2)": int(gl2),
            "F_calculado": f_calc,
            "F_crítico": f_crit,
            "Nível de Significância (α)": alpha
        }
        
        return resultado
    
    except ValueError as e:
        print(f"❌ Erro na validação: {e}")
        return None


# ============================================================================
# MENU INTERATIVO
# ============================================================================

def menu_principal():
    """
    Menu interativo para seleção de testes.
    """
    testes = {
        "1": ("Teste t para Média (Variância Desconhecida)", t_media_var_desconhecida),
        "2": ("Teste Z para Média (Variância Conhecida)", z_media_var_conhecida),
        "3": ("Teste Qui-Quadrado para Variância", chi2_variancia),
        "4": ("Teste Z para Proporção", z_proporcao),
        "5": ("Teste t para Diferença (Variâncias Desconhecidas e Iguais)", t_dif_medias_var_iguais),
        "6": ("Teste t de Welch (Variâncias DesconhecidasDiferentes)", t_welch_dif_medias),
        "7": ("Teste t Pareado", t_pareado),
        "8": ("Teste Z para Diferença de Médias (Variâncias Conhecidas)", z_dif_medias_var_conhecidas),
        "9": ("Teste Z para Diferença de Proporções", z_dif_proporcoes),
        "10": ("Teste F para Diferença entre Variâncias", f_dif_variancias),
    }
    
    while True:
        print("\n" + "="*60)
        print("CALCULADORA ESTATÍSTICA - TESTES DE HIPÓTESES")
        print("="*60)
        print("\nEscolha um teste:\n")
        
        for chave, (nome, _) in testes.items():
            print(f"{chave}. {nome}")
        
        print("\n0. Sair")
        print("-"*60)
        
        escolha = input("\nDigite a opção (0-10): ").strip()
        
        if escolha == "0":
            print("\n✓ Programa finalizado.")
            break
        
        if escolha not in testes:
            print("\n❌ Opção inválida. Tente novamente.")
            continue
        
        # Executa o teste selecionado
        nome_teste, funcao_teste = testes[escolha]
        resultado = funcao_teste()
        
        if resultado:
            print(formatar_resultado(resultado))
        
        # Oferece opção de repetir
        repetir = input("\nDeseja executar outro teste? (s/n): ").lower().strip()
        if repetir != "s":
            print("\n✓ Programa finalizado.")
            break


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    menu_principal()
