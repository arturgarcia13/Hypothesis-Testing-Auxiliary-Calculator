#!/usr/bin/env python3
"""
Script de setup rápido para a Calculadora de Testes de Hipóteses.

Este script verifica e instala as dependências necessárias.
"""

import sys
import subprocess
import pkg_resources

def verificar_python():
    """Verifica se a versão do Python é compatível."""
    versao_minima = (3, 13)
    versao_atual = sys.version_info[:2]
    
    if versao_atual < versao_minima:
        print(f"❌ Python {versao_minima[0]}.{versao_minima[1]}+ é necessário.")
        print(f"   Versão atual: {versao_atual[0]}.{versao_atual[1]}")
        return False
    
    print(f"✅ Python {versao_atual[0]}.{versao_atual[1]} - OK")
    return True

def verificar_dependencias():
    """Verifica se as dependências estão instaladas."""
    dependencias = ['numpy', 'scipy']
    faltando = []
    
    for dep in dependencias:
        try:
            pkg_resources.get_distribution(dep)
            print(f"✅ {dep} - Instalado")
        except pkg_resources.DistributionNotFound:
            print(f"❌ {dep} - Não encontrado")
            faltando.append(dep)
    
    return faltando

def instalar_dependencias(faltando):
    """Instala as dependências que estão faltando."""
    if not faltando:
        return True
    
    print(f"\n📦 Instalando dependências: {', '.join(faltando)}")
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ Dependências instaladas com sucesso!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Erro ao instalar dependências.")
        print("   Tente executar manualmente: pip install -r requirements.txt")
        return False

def main():
    """Função principal do setup."""
    print("🔧 SETUP - Calculadora de Testes de Hipóteses")
    print("=" * 50)
    
    # Verificar Python
    if not verificar_python():
        return 1
    
    # Verificar dependências
    print("\n📋 Verificando dependências...")
    faltando = verificar_dependencias()
    
    # Instalar se necessário
    if faltando:
        if not instalar_dependencias(faltando):
            return 1
    
    print("\n🎉 Setup concluído com sucesso!")
    print("   Para executar: python calculadora_testes_hipoteses.py")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())