import time

# ==============================================================================
# SCRIPT DE AUTOMAÇÃO DE TESTES - PROJETO SGHSS
# ==============================================================================
# Este script simula a execução de testes automatizados de interface (UI)
# e gera configurações para testes de carga, atendendo aos requisitos de QA.
#
# Ferramentas Simuladas: Selenium WebDriver (UI) e JMeter (Carga).
# ==============================================================================

class MockWebDriver:
    """Simula o comportamento do Selenium WebDriver para fins acadêmicos."""
    def get(self, url):
        print(f"[SELENIUM] Navegando para: {url}")
        time.sleep(0.8)

    def find_element_by_id_and_send_keys(self, element_id, text):
        print(f"[SELENIUM] Encontrado elemento '#{element_id}'. Digitando: '****' (Oculto)")
        time.sleep(0.3)

    def click_button(self, button_id):
        print(f"[SELENIUM] Clicando no botão '#{button_id}'")
        time.sleep(0.5)

def executar_teste_login_seguranca():
    print("\n========================================================")
    print(" EXECUTANDO BATERIA DE TESTES DE SEGURANÇA (AUTOMATIZADO)")
    print("========================================================")
    print("CASO DE TESTE: CT001 - Tentativa de Acesso Não Autorizado")
    print("OBJETIVO: Validar se o sistema bloqueia credenciais inválidas.")
    print("--------------------------------------------------------")

    # Inicialização do Driver
    driver = MockWebDriver()
    
    # Passo 1: Acessar página
    driver.get("https://sistema.vidaplus.com.br/login")

    # Passo 2: Inserir dados inválidos
    usuario = "admin_teste"
    senha_fraca = "12345" 
    
    driver.find_element_by_id_and_send_keys("input_user", usuario)
    driver.find_element_by_id_and_send_keys("input_pass", senha_fraca)
    
    # Passo 3: Tentar logar
    driver.click_button("btn_login")

    # Passo 4: Validação (Assertion)
    print("\n[QA-CORE] Analisando resposta do sistema...")
    time.sleep(1)
    
    msg_recebida = "Erro: Usuário ou senha inválidos."
    msg_esperada = "Erro: Usuário ou senha inválidos."

    if msg_recebida == msg_esperada:
        print(f"   [v] SUCESSO: Mensagem de erro correta exibida.")
        print(f"   [v] SUCESSO: Acesso ao sistema negado.")
        print(">> RESULTADO CT001: APROVADO")
    else:
        print(f"   [X] FALHA: O sistema permitiu acesso indevido.")
        print(">> RESULTADO CT001: REPROVADO")

def executar_simulacao_carga_jmeter():
    print("\n========================================================")
    print(" GERANDO CONFIGURAÇÃO DE TESTE DE CARGA (JMETER)")
    print("========================================================")
    print("CASO DE TESTE: TNF01 - Pico de Acessos em Prontuários")
    
    config = {
        "Target Host": "sistema.vidaplus.com.br",
        "Protocol": "HTTPS",
        "Port": 443,
        "Threads (Users)": 500,
        "Ramp-Up Period": "60s",
        "Duration": "300s",
        "Assert": "Response Time < 2000ms"
    }
    
    print(f"[JMETER-CONFIG] Configuração gerada para exportação (.jmx):")
    for key, value in config.items():
        print(f"   - {key}: {value}")
    
    print(">> STATUS: PRONTO PARA EXECUÇÃO EM AMBIENTE DE STAGING")

if __name__ == "__main__":
    executar_teste_login_seguranca()
    executar_simulacao_carga_jmeter()
    print("\n========================================================")
    print(" FIM DO RELATÓRIO DE EXECUÇÃO")
    print("========================================================")

# ==============================================================================
# IDENTIFICAÇÃO DO ALUNO - TRABALHO DE CONCLUSÃO DE DISCIPLINA
# ==============================================================================
# Nome: Renan da Rosa de Oliveira
# RU: 4635549
# Polo: LONDRINA/PR EAD
# Curso: Análise e Desenvolvimento de Sistemas
# Disciplina: Projeto Multidisciplinar (Gestão Hospitalar - SGHSS)
# Ênfase: Qualidade de Software (QA)
# ==============================================================================