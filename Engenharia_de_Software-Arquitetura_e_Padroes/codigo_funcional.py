from abc import ABC, abstractmethod
from datetime import datetime, time, timedelta
import re
import time as tm
# import keyboard as kb -> linha comentada porque nessa pasta nao tenho a biblioteca insalada

tempo_soneca = 5
tempo_espera_soneca = 5

# Classe Context
class Despertador:
    """Contexto que mantém o estado atual do despertador."""

    def __init__(self):
        self._estado = Desarmado()  # Estado inicial: desarmado
        self._sonecas = 0  # Contador de sonecas feitas (máximo 3)
        self._hora_alarme = None  # Horário settado para o alarme

    def set_estado(self, estado):
        """Muda o estado do despertador."""
        self._estado = estado
        print(f"Estado alterado para: {type(estado).__name__}")

    def checar_estado(self):
        return type(self._estado).__name__

    def armar_alarme(self, soneca=False):
        """Delegação da ação de armar o alarme do despertador."""
        self._estado.armar_alarme(self, soneca)

    def checar_alarme(self):
        """Delegação da ação de checar se o horário do alarme chegou."""
        self._estado.checar_alarme(self)

    def tocar_alarme(self, desativar=False):
        """Delegação da ação de tocar o alarme no horário."""
        self._estado.tocar_alarme(self, desativar)


# Classe abstrata State
class State(ABC):
    """Interface para os estados da máquina."""

    @abstractmethod
    def armar_alarme(self, machine: Despertador, soneca=False):
        pass

    @abstractmethod
    def checar_alarme(self, machine: Despertador):
        pass

    @abstractmethod
    def tocar_alarme(self, machine: Despertador, desativar=False):
        pass


# Estado: Desarmado
class Desarmado(State):
    def armar_alarme(self, machine: Despertador, soneca=False):
        if soneca:
            # print(f"Estado alterado para: Esperando - Soneca")
            if machine._hora_alarme is None:
                print("Erro: nenhum alarme configurado")
                return
            if machine._sonecas >= 3:
                print("Limite de sonecas atingido (máximo 3). Alarme desativado.")
                machine._sonecas = 0  # Resetar contador
                machine._hora_alarme = None
                return
            # Adicionar 5 minutos para soneca
            current_datetime = datetime.combine(datetime.today(), machine._hora_alarme)
            nova_hora_alarme = current_datetime + timedelta(minutes=tempo_soneca)
            machine._hora_alarme = nova_hora_alarme.time()
            machine._sonecas += 1
            print(
                f"Modo soneca ativado ({machine._sonecas}/3). Novo horário: {machine._hora_alarme.hour:02d}:{machine._hora_alarme.minute:02d}")
            machine.set_estado(Esperando())
            return

        # Configuração normal do alarme
        print("Defina o horário do alarme (HH:MM, ex: 14:30): ")
        while True:
            horario_user = input("> ")
            if not re.match(r"^\d{2}:\d{2}$", horario_user):
                print("Formato inválido. Use HH:MM (ex.: 04:50).")
                continue
            try:
                # Convertendo a String pro objeto time
                hora_alarme = datetime.strptime(horario_user, "%H:%M").time()
                machine._hora_alarme = hora_alarme
                machine._sonecas = 0  # Resetar contador de sonecas
                print(f"Alarme configurado para {horario_user}.")
                machine.set_estado(Esperando())
                break
            except ValueError:
                print("Horário inválido. Tente novamente (ex.: 14:30).")

    def checar_alarme(self, machine: Despertador):
        print("Erro: configure um alarme primeiro.")

    def tocar_alarme(self, machine: Despertador, desativar=False):
        print("Erro: configure um alarme primeiro.")


# Estado: Esperando
class Esperando(State):
    def armar_alarme(self, machine: Despertador, soneca=False):
        print("Alarme já configurado. Deseja reconfigurar? (s/n)")
        if input("> ").lower() == 's':
            machine.set_estado(Desarmado())
            machine.armar_alarme()

    def checar_alarme(self, machine: Despertador):
        hora_atual = datetime.now().time()
        hora_alarme = machine._hora_alarme
        """print(f"{hora_atual.hour:02d}:{hora_atual.minute:02d} - hora atual")
        print(f"{hora_alarme.hour:02d}:{hora_alarme.minute:02d} - hora alarme")"""
        if hora_atual.hour == hora_alarme.hour and hora_atual.minute == hora_alarme.minute:
            machine.set_estado(TocandoAlarme())
            machine.tocar_alarme()

    def tocar_alarme(self, machine: Despertador, desativar=False):
        if desativar:
            machine.set_estado(TocandoAlarme())
            machine.tocar_alarme(desativar=True)
            return
        print("Erro: o alarme ainda não chegou no horário configurado.")


# Estado: Tocando alarme
class TocandoAlarme(State):
    def armar_alarme(self, machine: Despertador, soneca=False):
        print("Alarme já disparado. Configure um novo.")
        machine.set_estado(Desarmado())
        machine.armar_alarme()

    def checar_alarme(self, machine: Despertador):
        print("Alarme já disparado. Configure um novo.")

    def tocar_alarme(self, machine: Despertador, desativar=False):
        print("=" * 10 + " ALARME DISPARADO " + "=" * 10)
        print("Digite 'd' para desativar, 's' para soneca (5 minutos), ou aguarde 5 segundos para soneca automática.")

        # Dar x segundos para o usuário responder
        start_time = tm.time()
        while tm.time() - start_time < tempo_espera_soneca:
            if kb.is_pressed('d') or desativar:
                print("\nAlarme desativado.")
                machine._sonecas = 0  # Resetar contador de sonecas
                machine._hora_alarme = None
                machine.set_estado(Desarmado())
                tm.sleep(0.2)  # Evitar múltiplas detecções
                return
            elif kb.is_pressed('s'):
                print("\nModo soneca ativado.")
                machine.set_estado(Desarmado())
                machine.armar_alarme(soneca=True)
                tm.sleep(0.2)  # Evitar múltiplas detecções
                return
            tm.sleep(0.1)  # Evitar uso excessivo de CPU

        # Se passar 5 segundos sem entrada válida, ativar soneca
        print("Nenhum input válido. Ativando modo soneca automaticamente...")
        machine.set_estado(Desarmado())
        machine.armar_alarme(soneca=True)


# Código do cliente
if __name__ == "__main__":
    alarme = Despertador()

    while True:
        print("\nBem vindo ao alarme: \n"
              "1 - Armar alarme; \n"
              "2 - sair")
        rep = input("> ")
        if rep == '1':
            # Configurar o alarme
            alarme.armar_alarme()

            # Simular verificação do alarme em loop
            print("Digite 'd' para desativar o alarme")
            while True:
                if alarme.checar_estado() == 'Desarmado':
                    break
                start_time = tm.time()
                alarme.checar_alarme()
                while tm.time() - start_time < 5:
                    if kb.is_pressed('d'):
                        print("O alarme será desativado.")
                        alarme.tocar_alarme(desativar=True)
                        break
                tm.sleep(0.1)  # Evita uso extremo de CPU
                # Para simulação, você pode configurar o horário do alarme próximo ao atual
        if rep == '2':
            print("Você escolheu sair.")
            break



