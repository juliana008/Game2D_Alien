from types import SimpleNamespace

import pygame
import pytest

from fast_alien import FastAlien
from fleet_manager import FleetManager
from settings import Settings


@pytest.fixture
def game_objects(
    monkeypatch: pytest.MonkeyPatch,
) -> tuple[pygame.Surface, Settings, SimpleNamespace]:
    settings = Settings()
    settings.screen_width = 120
    settings.screen_height = 100
    screen = pygame.Surface((settings.screen_width, settings.screen_height))
    ship = SimpleNamespace(rect=pygame.Rect(50, 80, 20, 20))
    monkeypatch.setattr(
        pygame.image,
        "load",
        lambda _: pygame.Surface((10, 10)),
    )
    return screen, settings, ship


def test_fast_alien_moves_twice_as_fast_as_base_alien(
    game_objects: tuple[pygame.Surface, Settings, SimpleNamespace],
) -> None:
    screen, settings, _ = game_objects
    alien = FastAlien(screen, settings)
    initial_x = alien.x

    alien.update()

    assert alien.x == initial_x + 2 * settings.alien_speed


def test_fleet_manager_accepts_fast_alien_subclass(
    game_objects: tuple[pygame.Surface, Settings, SimpleNamespace],
) -> None:
    screen, settings, ship = game_objects
    fleet = FleetManager(screen, settings, ship, FastAlien)
    fleet.create_fleet()
    initial_x = fleet.aliens.sprites()[0].x

    fleet._update_aliens()

    assert all(isinstance(alien, FastAlien) for alien in fleet.aliens)
    assert fleet.aliens.sprites()[0].x == initial_x + 2 * settings.alien_speed
