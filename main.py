#!/usr/bin/env python3
"""
Exemplo de código Python - Demonstração de conceitos básicos
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional

class GerenciadorTarefas:
    """Classe para gerenciar uma lista de tarefas"""
    
    def __init__(self):
        self.tarefas: List[Dict] = []
        self.arquivo = "tarefas.json"
        self.carregar_tarefas()
    
    def adicionar_tarefa(self, titulo: str, descricao: str = "", prioridade: str = "baixa") -> None:
        """Adiciona uma nova tarefa"""
        tarefa = {
            "id": len(self.tarefas) + 1,
            "titulo": titulo,
            "descricao": descricao,
            "prioridade": prioridade,
            "concluida": False,
            "data_criacao": datetime.now().isoformat()
        }
        self.tarefas.append(tarefa)
        print(f"✅ Tarefa '{titulo}' adicionada com sucesso!")
        self.salvar_tarefas()
    
    def listar_tarefas(self, apenas_pendentes: bool = False) -> None:
        """Lista todas as tarefas ou apenas as pendentes"""
        if not self.tarefas:
            print("📝 Nenhuma tarefa encontrada.")
            return
        
        tarefas_filtradas = self.tarefas
        if apenas_pendentes:
            tarefas_filtradas = [t for t in self.tarefas if not t["concluida"]]
        
        print("\n📋 Lista de Tarefas:")
        print("-" * 60)
        
        for tarefa in tarefas_filtradas:
            status = "✅" if tarefa["concluida"] else "⏳"
            prioridade_emoji = {"alta": "🔴", "media": "🟡", "baixa": "🟢"}.get(tarefa["prioridade"], "⚪")
            
            print(f"{status} {prioridade_emoji} [{tarefa['id']}] {tarefa['titulo']}")
            if tarefa["descricao"]:
                print(f"   📄 {tarefa['descricao']}")
            print(f"   📅 Criada em: {tarefa['data_criacao'][:10]}")
            print()
    
    def marcar_concluida(self, tarefa_id: int) -> None:
        """Marca uma tarefa como concluída"""
        for tarefa in self.tarefas:
            if tarefa["id"] == tarefa_id:
                tarefa["concluida"] = True
                print(f"✅ Tarefa '{tarefa['titulo']}' marcada como concluída!")
                self.salvar_tarefas()
                return
        print(f"❌ Tarefa com ID {tarefa_id} não encontrada.")
    
    def remover_tarefa(self, tarefa_id: int) -> None:
        """Remove uma tarefa da lista"""
        for i, tarefa in enumerate(self.tarefas):
            if tarefa["id"] == tarefa_id:
                titulo = tarefa["titulo"]
                del self.tarefas[i]
                print(f"🗑️ Tarefa '{titulo}' removida!")
                self.salvar_tarefas()
                return
        print(f"❌ Tarefa com ID {tarefa_id} não encontrada.")
    
    def salvar_tarefas(self) -> None:
        """Salva as tarefas em um arquivo JSON"""
        try:
            with open(self.arquivo, 'w', encoding='utf-8') as f:
                json.dump(self.tarefas, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"❌ Erro ao salvar tarefas: {e}")
    
    def carregar_tarefas(self) -> None:
        """Carrega as tarefas de um arquivo JSON"""
        if os.path.exists(self.arquivo):
            try:
                with open(self.arquivo, 'r', encoding='utf-8') as f:
                    self.tarefas = json.load(f)
                print(f"📂 {len(self.tarefas)} tarefas carregadas do arquivo.")
            except Exception as e:
                print(f"❌ Erro ao carregar tarefas: {e}")
                self.tarefas = []
        else:
            print("📝 Nenhum arquivo de tarefas encontrado. Iniciando com lista vazia.")

def calcular_estatisticas(numeros: List[float]) -> Dict[str, float]:
    """Calcula estatísticas básicas de uma lista de números"""
    if not numeros:
        return {}
    
    return {
        "total": len(numeros),
        "soma": sum(numeros),
        "media": sum(numeros) / len(numeros),
        "minimo": min(numeros),
        "maximo": max(numeros),
        "mediana": sorted(numeros)[len(numeros) // 2]
    }

def fibonacci(n: int) -> List[int]:
    """Gera a sequência de Fibonacci até n termos"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib

def menu_principal():
    """Menu principal da aplicação"""
    gerenciador = GerenciadorTarefas()
    
    while True:
        print("\n" + "="*50)
        print("🐍 APLICAÇÃO PYTHON - GERENCIADOR DE TAREFAS")
        print("="*50)
        print("1. ➕ Adicionar tarefa")
        print("2. 📋 Listar todas as tarefas")
        print("3. ⏳ Listar tarefas pendentes")
        print("4. ✅ Marcar tarefa como concluída")
        print("5. 🗑️ Remover tarefa")
        print("6. 📊 Demonstrar funções matemáticas")
        print("7. 🚪 Sair")
        
        try:
            opcao = input("\n👉 Escolha uma opção (1-7): ").strip()
            
            if opcao == "1":
                titulo = input("📝 Título da tarefa: ").strip()
                if titulo:
                    descricao = input("📄 Descrição (opcional): ").strip()
                    prioridade = input("🎯 Prioridade (alta/media/baixa) [baixa]: ").strip().lower() or "baixa"
                    if prioridade not in ["alta", "media", "baixa"]:
                        prioridade = "baixa"
                    gerenciador.adicionar_tarefa(titulo, descricao, prioridade)
                else:
                    print("❌ Título não pode estar vazio!")
            
            elif opcao == "2":
                gerenciador.listar_tarefas()
            
            elif opcao == "3":
                gerenciador.listar_tarefas(apenas_pendentes=True)
            
            elif opcao == "4":
                try:
                    tarefa_id = int(input("🔢 ID da tarefa para marcar como concluída: "))
                    gerenciador.marcar_concluida(tarefa_id)
                except ValueError:
                    print("❌ Por favor, digite um número válido!")
            
            elif opcao == "5":
                try:
                    tarefa_id = int(input("🔢 ID da tarefa para remover: "))
                    gerenciador.remover_tarefa(tarefa_id)
                except ValueError:
                    print("❌ Por favor, digite um número válido!")
            
            elif opcao == "6":
                print("\n🔢 Demonstração de Funções Matemáticas:")
                print("-" * 40)
                
                # Fibonacci
                try:
                    n = int(input("📊 Quantos termos de Fibonacci gerar? "))
                    if n > 0:
                        fib_seq = fibonacci(n)
                        print(f"🔗 Fibonacci ({n} termos): {fib_seq}")
                    else:
                        print("❌ Por favor, digite um número positivo!")
                except ValueError:
                    print("❌ Por favor, digite um número válido!")
                
                # Estatísticas
                print("\n📈 Calculadora de Estatísticas:")
                numeros_input = input("🔢 Digite números separados por espaço: ").strip()
                if numeros_input:
                    try:
                        numeros = [float(x) for x in numeros_input.split()]
                        stats = calcular_estatisticas(numeros)
                        print("\n📊 Estatísticas:")
                        for chave, valor in stats.items():
                            print(f"   {chave.capitalize()}: {valor:.2f}")
                    except ValueError:
                        print("❌ Por favor, digite apenas números válidos!")
            
            elif opcao == "7":
                print("👋 Obrigado por usar o Gerenciador de Tarefas!")
                break
            
            else:
                print("❌ Opção inválida! Por favor, escolha entre 1-7.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário. Até logo!")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    print("🚀 Iniciando aplicação Python...")
    menu_principal()