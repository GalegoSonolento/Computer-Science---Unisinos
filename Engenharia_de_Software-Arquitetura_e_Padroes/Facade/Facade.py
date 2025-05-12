from abc import ABC, abstractmethod

class HomeTheaterComponent(ABC):
    """Abstract base class for home theater components.

    Defines a common interface for all components, ensuring they support
    turning on, turning off, and displaying parameters.
    """
    
    @abstractmethod
    def on(self):
        """Turn on the component."""
        pass

    @abstractmethod
    def off(self):
        """Turn off the component."""
        pass

    @abstractmethod
    def show_parameters(self):
        """Display the component's current parameters."""
        pass

class HomeTheaterFacade:
    """Facade to simplify home theater system operations.

    Provides a unified interface to control multiple subsystems, such as
    lights, projector, amplifier, and SmartTV, for watching movies.
    """
    
    def __init__(self):
        """Initialize all subsystems of the home theater."""
        self.subsystems = {
            "theater_lights": TheaterLights(),
            "room_lights": RoomLights(),
            "projector": Projector(),
            "amplifier": Amplifier(),
            "smart_tv": SmartTV()
        }

    def watch_movie(self, show_name):
        """Start watching a movie with optimal subsystem settings.

        Args:
            show_name (str or int): Name or code of the show to play on Netflix.

        Raises:
            ValueError: If show_name is empty or not a string or integer.

        Configures theater lights, room lights, projector, amplifier, and SmartTV.
        """
        if not show_name or not isinstance(show_name, (int, str)):
            raise ValueError("Nome do programa deve ser uma String não-vazia ou um Integer.")

        print(f"Preparando-se para assistir à {show_name}")
        # Configuration luminosidade do Home Theater
        self.subsystems["theater_lights"].on()
        self.subsystems["theater_lights"].dim(20)

        # Desligando as luzes da sala
        self.subsystems["room_lights"].off()

        # Ligando o projetor
        self.subsystems["projector"].on()
        self.subsystems["projector"].wide_screen_mode()

        # Ligando amplificador
        self.subsystems["amplifier"].on()
        self.subsystems["amplifier"].set_volume(23)

        # Ligando SmartTV
        self.subsystems["smart_tv"].on()
        self.subsystems["smart_tv"].play_netflix(show_name)

    def end_movie(self):
        """Shut down the home theater system and reset subsystems.

        Turns off theater lights, projector, amplifier, and SmartTV, and
        turns on room lights to restore the initial state.
        """
        # Desligando luminosidade do Home Theater
        self.subsystems["theater_lights"].off()

        # Ligando luzes da sala
        self.subsystems["room_lights"].on()

        # Desligando projetor
        self.subsystems["projector"].off()

        # Desligando amplificador
        self.subsystems["amplifier"].off()

        # Desligando SmartTV
        self.subsystems["smart_tv"].off()

class SmartTV(HomeTheaterComponent):
    """SmartTV component for playing Netflix content in the home theater.

    Manages TV power state and Netflix playback, including play, pause, and resume.
    """
    
    def __init__(self):
        """Initialize the SmartTV with default settings."""
        self.turned_on = False
        self.netflixState = "off"  # Possible states: off, on, playing
        self.netflixShowCode = 0
    
    def on(self):
        """Turn on the SmartTV."""
        self.turned_on = True
        print("SmartTV ligada!")
    
    def play_netflix(self, cod):
        """Play a show on Netflix.

        Args:
            cod (str or int): Show name or code to play.

        Raises:
            ValueError: If the TV is off or cod is not a string or integer.
        """
        if not self.turned_on:
            raise ValueError("SmartTV precisa estar ligada para assistir à Netflix")
        if not isinstance(cod, (int, str)):
            raise ValueError("Código do programa deve ser uma String ou integer")
        self.netflixShowCode = cod
        self.netflixState = "playing"
        print(f"Tocando programa '{self.netflixShowCode}' na Netflix agora!")
    
    def stop_netflix(self):
        """Pause Netflix playback.

        Raises:
            ValueError: If the TV is off or Netflix is not playing.
        """
        if not self.turned_on:
            raise ValueError("SmartTV precisa estar ligada para pausar a Netflix")
        if self.netflixState != "playing":
            raise ValueError("Netflix não está tocando para ser pausada.")
        self.netflixState = "on"
        print("Netflix pausada!")

    def resume_netflix(self):
        """Resume Netflix playback.

        Raises:
            ValueError: If the TV is off or Netflix is not paused.
        """
        if not self.turned_on:
            raise ValueError("SmartTV precisa estar ligada para dar play à Netflix")
        if self.netflixState != "on":
            raise ValueError("A Netflix não está pausada para ser retomada.")
        self.netflixState = "playing"
        print(f"Prosseguindo com programa {self.netflixShowCode}!")

    def off(self):
        """Turn off the SmartTV and reset Netflix settings."""
        self.netflixState = "off"
        self.netflixShowCode = 0
        self.turned_on = False
        print("SmartTV e Netflix desligados!")
    
    def show_parameters(self):
        """Display the current state of the SmartTV."""
        print(f"turned_on: {self.turned_on}")
        print(f"netflixState: {self.netflixState}")
        print(f"netflixShowCode: {self.netflixShowCode}")

class Amplifier(HomeTheaterComponent):
    """Amplifier component for controlling audio in the home theater."""
    
    def __init__(self):
        """Initialize the amplifier with default settings."""
        self.turned_on = False
        self.volumeLevel = 0
    
    def on(self):
        """Turn on the amplifier."""
        self.turned_on = True
        print("Amplificador ligado!")
    
    def set_volume(self, level):
        """Set the amplifier volume.

        Args:
            level (int): Volume level to set (0 to 100).

        Raises:
            ValueError: If level is not an integer or not in range [0, 100].
        """
        if not isinstance(level, int) or level < 0 or level > 100:
            raise ValueError("Volume deve ser um valor inteiro positivo (non-negative Integer)")
        self.volumeLevel = level
        print(f"Volume alterado para {self.volumeLevel}!")
    
    def off(self):
        """Turn off the amplifier and reset volume."""
        self.turned_on = False
        self.volumeLevel = 0

    def show_parameters(self):
        """Display the current state of the amplifier."""
        print(f"turned_on: {self.turned_on}")
        print(f"volumeLevel: {self.volumeLevel}")

class RoomLights(HomeTheaterComponent):
    """Room lights component for controlling ambient lighting."""
    
    def __init__(self):
        """Initialize room lights (on by default)."""
        self.room_lights = True
    
    def on(self):
        """Turn on the room lights."""
        self.room_lights = True
        print("Luzes da sala ligadas!")

    def off(self):
        """Turn off the room lights."""
        self.room_lights = False
        print("Luzes da sala desligadas!")

    def show_parameters(self):
        """Display the current state of the room lights."""
        print(f"room_lights: {self.room_lights}")

class Projector(HomeTheaterComponent):
    """Projector component for displaying video content."""
    
    def __init__(self):
        """Initialize the projector with default settings."""
        self.turned_on = False
        self.wide_screen_mode_on = False
    
    def on(self):
        """Turn on the projector."""
        self.turned_on = True
        print("Projetor ligado!")
    
    def wide_screen_mode(self):
        """Toggle wide screen mode.

        Raises:
            ValueError: If the projector is off.
        """
        if not self.turned_on:
            raise ValueError("Projetor deve estar ligado para mudar o modo de projeção")
        self.wide_screen_mode_on = not self.wide_screen_mode_on
        print(f"Modo widescreen {'ativado' if self.wide_screen_mode_on else 'desativado'}")

    def off(self):
        """Turn off the projector and reset wide screen mode."""
        self.turned_on = False
        self.wide_screen_mode_on = False
        print("Projetor desligado!")

    def show_parameters(self):
        """Display the current state of the projector."""
        print(f"turned_on: {self.turned_on}")
        print(f"wide_screen_mode_on: {self.wide_screen_mode_on}")

class TheaterLights(HomeTheaterComponent):
    """Theater lights component for controlling ambiance lighting."""
    
    def __init__(self):
        """Initialize theater lights with default settings."""
        self.theater_lights_on = False
        self.dim_level = 100
    
    def on(self):
        """Turn on the theater lights."""
        self.theater_lights_on = True
        print("Luzes de HomeTheater ligadas!")
    
    def off(self):
        """Turn off the theater lights."""
        self.theater_lights_on = False
        print("Luzes de HomeTheater desligadas!")
    
    def dim(self, level):
        """Set the dim level of the theater lights.

        Args:
            level (int): Dim level to set (0 to 100).

        Raises:
            ValueError: If level is not an integer or not in range [0, 100].
        """
        if not isinstance(level, int) or level < 0 or level > 100:
            raise ValueError("Intensidade da luz deve ser um inteiro entre 0 e 100.")
        self.dim_level = level
        print(f"Intensidade da luz configurada para {self.dim_level}!")

    def show_parameters(self):
        """Display the current state of the theater lights."""
        print(f"theater_lights_on: {self.theater_lights_on}")
        print(f"dim_level: {self.dim_level}")

if __name__ == "__main__":
    home_theater = HomeTheaterFacade()

    show_name = str(input("Digite o nome do programa que deseja assistir: "))
    home_theater.watch_movie(show_name)
    input("Pressione qualquer tecla para desligar o HomeTheater... ")
    home_theater.end_movie()