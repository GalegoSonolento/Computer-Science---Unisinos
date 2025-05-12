# test_home_theater.py
import pytest
from Facade import HomeTheaterFacade, SmartTV, Amplifier, RoomLights, Projector, TheaterLights

# Fixture to create a HomeTheaterFacade instance
@pytest.fixture
def facade():
    return HomeTheaterFacade()

# Fixture to create subsystem instances
@pytest.fixture
def smart_tv():
    return SmartTV()

@pytest.fixture
def amplifier():
    return Amplifier()

@pytest.fixture
def room_lights():
    return RoomLights()

@pytest.fixture
def projector():
    return Projector()

@pytest.fixture
def theater_lights():
    return TheaterLights()

# Tests for HomeTheaterFacade
def test_watch_movie_success(facade, capsys):
    facade.watch_movie("Inception")
    captured = capsys.readouterr()
    assert "Preparando-se para assistir à Inception" in captured.out
    assert facade.subsystems["smart_tv"].turned_on
    assert facade.subsystems["smart_tv"].netflixState == "playing"
    assert facade.subsystems["smart_tv"].netflixShowCode == "Inception"
    assert facade.subsystems["projector"].turned_on
    assert facade.subsystems["projector"].wide_screen_mode_on
    assert facade.subsystems["amplifier"].turned_on
    assert facade.subsystems["amplifier"].volumeLevel == 23
    assert facade.subsystems["theater_lights"].theater_lights_on
    assert facade.subsystems["theater_lights"].dim_level == 20
    assert not facade.subsystems["room_lights"].room_lights

def test_watch_movie_invalid_show_name(facade):
    with pytest.raises(ValueError, match="Nome do programa deve ser uma String não-vazia."):
        facade.watch_movie("")
    with pytest.raises(ValueError, match="Nome do programa deve ser uma String não-vazia."):
        facade.watch_movie(None)

def test_end_movie(facade):
    facade.watch_movie("Inception")  # Set up state
    facade.end_movie()
    assert not facade.subsystems["smart_tv"].turned_on
    assert facade.subsystems["smart_tv"].netflixState == "off"
    assert facade.subsystems["smart_tv"].netflixShowCode == 0
    assert not facade.subsystems["projector"].turned_on
    assert not facade.subsystems["projector"].wide_screen_mode_on
    assert not facade.subsystems["amplifier"].turned_on
    assert facade.subsystems["amplifier"].volumeLevel == 0
    assert not facade.subsystems["theater_lights"].theater_lights_on
    assert facade.subsystems["room_lights"].room_lights

# Tests for SmartTV
def test_smart_tv_on_off(smart_tv):
    smart_tv.on()
    assert smart_tv.turned_on
    smart_tv.off()
    assert not smart_tv.turned_on
    assert smart_tv.netflixState == "off"
    assert smart_tv.netflixShowCode == 0

def test_smart_tv_play_netflix(smart_tv):
    smart_tv.on()
    smart_tv.play_netflix("Stranger Things")
    assert smart_tv.netflixState == "playing"
    assert smart_tv.netflixShowCode == "Stranger Things"

def test_smart_tv_play_netflix_not_on(smart_tv):
    with pytest.raises(ValueError, match="SmartTV precisa estar ligada para assistir à Netflix"):
        smart_tv.play_netflix("Stranger Things")

def test_smart_tv_invalid_netflix_code(smart_tv):
    smart_tv.on()
    with pytest.raises(ValueError, match="Código do programa deve ser uma String ou integer"):
        smart_tv.play_netflix(None)

def test_smart_tv_stop_resume_netflix(smart_tv):
    smart_tv.on()
    smart_tv.play_netflix("Stranger Things")
    smart_tv.stop_netflix()
    assert smart_tv.netflixState == "on"
    smart_tv.resume_netflix()
    assert smart_tv.netflixState == "playing"

# Tests for Amplifier
def test_amplifier_on_off(amplifier):
    amplifier.on()
    assert amplifier.turned_on
    amplifier.off()
    assert not amplifier.turned_on
    assert amplifier.volumeLevel == 0

def test_amplifier_set_volume(amplifier):
    amplifier.on()
    amplifier.set_volume(50)
    assert amplifier.volumeLevel == 50

def test_amplifier_invalid_volume(amplifier):
    amplifier.on()
    with pytest.raises(ValueError, match="Volume deve ser um valor inteiro positivo"):
        amplifier.set_volume(-1)

# Tests for RoomLights
def test_room_lights_on_off(room_lights):
    room_lights.off()
    assert not room_lights.room_lights
    room_lights.on()
    assert room_lights.room_lights

# Tests for Projector
def test_projector_on_off(projector):
    projector.on()
    assert projector.turned_on
    projector.off()
    assert not projector.turned_on
    assert not projector.wide_screen_mode_on

def test_projector_wide_screen_mode(projector):
    projector.on()
    projector.wide_screen_mode()
    assert projector.wide_screen_mode_on
    projector.wide_screen_mode()
    assert not projector.wide_screen_mode_on

def test_projector_wide_screen_mode_not_on(projector):
    with pytest.raises(ValueError, match="Projetor deve estar ligado para mudar o modo de projeção"):
        projector.wide_screen_mode()

# Tests for TheaterLights
def test_theater_lights_on_off(theater_lights):
    theater_lights.on()
    assert theater_lights.theater_lights_on
    theater_lights.off()
    assert not theater_lights.theater_lights_on

def test_theater_lights_dim(theater_lights):
    theater_lights.dim(50)
    assert theater_lights.dim_level == 50

def test_theater_lights_invalid_dim(theater_lights):
    with pytest.raises(ValueError, match="Intensidade da luz deve ser um inteiro entre 0 e 100."):
        theater_lights.dim(-1)
    with pytest.raises(ValueError, match="Intensidade da luz deve ser um inteiro entre 0 e 100."):
        theater_lights.dim(101)