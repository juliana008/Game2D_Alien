import pygame
import pytest

from settings import Settings
from ship import Ship


@pytest.fixture
def ship(monkeypatch: pytest.MonkeyPatch) -> Ship:
    settings = Settings()
    screen = pygame.Surface((settings.screen_width, settings.screen_height))
    monkeypatch.setattr(
        pygame.image,
        "load",
        lambda _: pygame.Surface((30, 20)),
    )
    return Ship(screen, settings)


def test_ship_starts_centered_at_bottom(ship: Ship) -> None:
    assert ship.rect.midbottom == ship.screen_rect.midbottom


def test_ship_moves_right_by_configured_speed(ship: Ship) -> None:
    initial_x = ship.x
    ship.moving_right = True

    ship.update()

    assert ship.x == initial_x + ship.settings.ship_speed


def test_ship_moves_left_by_configured_speed(ship: Ship) -> None:
    initial_x = ship.x
    ship.moving_left = True

    ship.update()

    assert ship.x == initial_x - ship.settings.ship_speed


def test_ship_does_not_move_past_left_edge(ship: Ship) -> None:
    ship.rect.left = 0
    ship.x = float(ship.rect.x)
    ship.moving_left = True

    ship.update()

    assert ship.rect.left == 0


def test_ship_does_not_move_past_right_edge(ship: Ship) -> None:
    ship.rect.right = ship.screen_rect.right
    ship.x = float(ship.rect.x)
    ship.moving_right = True

    ship.update()

    assert ship.rect.right == ship.screen_rect.right
