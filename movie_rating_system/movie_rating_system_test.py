from unittest import TestCase
from movie_rating_system import movies, ratings, add_movie, rate_movie, view_average_ratings

class TestMovieRatingSystem(TestCase):

    def setUp(self):
       
        movies.clear()
        ratings.clear()

    def test_add_movie(self):
        result = add_movie("Koto Aye")
        self.assertEqual(result, "Movie 'Koto Aye' added!")
        self.assertIn("Koto Aye", movies)

    def test_rate_movie(self):
        add_movie("Koto Aye")
        result = rate_movie("Koto Aye", 5)
        self.assertEqual(result, "Rating added for 'Koto Aye' 5")

    def test_invalid_rating(self):
        add_movie("Koto Aye")
        result = rate_movie("Koto Aye", 10)
        self.assertEqual(result, "Invalid rating! Enter a number from 1 to 5.")

    def test_view_average_ratings(self):
        add_movie("Inception")
        rate_movie("Inception", 5)
        rate_movie("Inception", 4)
        
        result = view_average_ratings()
        self.assertEqual(result, "Average Ratings:\nInception: 4.5")
