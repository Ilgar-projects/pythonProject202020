import pytest
from unittest.mock import MagicMock

from dao.model.movie import Movie
from dao.model.genre import Genre
from dao.model.director import Director
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture()
def movie_dao_fixture():
    movie_dao = MovieDAO(None)

    d1 = Director(id=1, name='test')
    g1 = Genre(id=1, name='test')

    red = Movie(
        id=1,
        title='RED',
        description='tes tes tes',
        trailer='test',
        year=2022,
        genre_id=1,
        genre=g1,
        director_id=d1
    )

    movie_dao.get_one = MagicMock(return_value=red)
    movie_dao.get_all = MagicMock(return_value=[red, ])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    # movie_dao.partially_update = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao_fixture):
        self.movie_service = MovieService(dao=movie_dao_fixture)

    def test_partially_update(self):
        movie_d = {
            'id': 1,
            'year': 2020
        }
        movie = self.movie_service.partially_update(movie_d)

        # assert movie.year == movie_d.get("year")


    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id == 1

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert movies is not None
        assert len(movies) == 1

    def test_create(self):
        movie = {
            'name': 'Rose',
        }
        self.movie_service.create(movie)

        assert movie is not None

    def test_update(self):
        movie = {
            'id': 1,
            'name': 'Rose',
        }
        self.movie_service.update(movie)

    def test_delete(self):
        self.movie_service.delete(1)
