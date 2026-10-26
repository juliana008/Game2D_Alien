import pygame
import pytest
from pytest_mock import MockerFixture

from bullet import Bullet
from bullet_manager import BulletManager
from settings import Settings
from tests.doubles import StubShip


@pytest.fixture
def game_objects() -> tuple[pygame.Surface, Settings, StubShip]:
    settings = Settings()
    screen = pygame.Surface((settings.screen_width, settings.screen_height))
    ship = StubShip(pygame.Rect(100, 300, 40, 20))
    return screen, settings, ship


def test_bullet_uses_stub_ship_position_and_moves_up(
    game_objects: tuple[pygame.Surface, Settings, StubShip],
) -> None:
    screen, settings, ship = game_objects
    bullet = Bullet(screen, settings, ship)

    assert bullet.rect.midtop == ship.rect.midtop

    bullet.update()

    assert bullet.y == ship.rect.top - settings.bullet_speed


def test_bullet_manager_requests_sprite_collision(
    game_objects: tuple[pygame.Surface, Settings, StubShip],
    mocker: MockerFixture,
) -> None:
    screen, settings, ship = game_objects
    manager = BulletManager(screen, settings, ship)
    aliens = pygame.sprite.Group()
    groupcollide = mocker.patch(
        "bullet_manager.pygame.sprite.groupcollide",
        return_value={},
    )

    manager._check_bullet_alien_collisions(aliens)

    groupcollide.assert_called_once_with(manager.bullets, aliens, True, True)
