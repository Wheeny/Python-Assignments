import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class MovieRatingSystemTest {

    @BeforeEach
    public void setUp() {
     
        MovieRatingSystem.movies.clear();
        MovieRatingSystem.ratings.clear();
    }

    @Test
    public void testAddMovie() {
        String result = MovieRatingSystem.addMovie("Koto Aye");
        assertEquals("Movie 'Koto Aye' added!", result);
        assertTrue(MovieRatingSystem.movies.contains("Koto Aye"));
    }

    @Test
    public void testRateMovie() {
        MovieRatingSystem.addMovie("Koto Aye");
        String result = MovieRatingSystem.rateMovie("Koto Aye", 5.0);
        assertEquals("Rating added for 'Koto Aye' 5.0", result);
    }

    @Test
    public void testInvalidRating() {
        MovieRatingSystem.addMovie("Koto Aye");
        String result = MovieRatingSystem.rateMovie("Koto Aye", 10.0);
        assertEquals("Invalid rating! Enter a number from 1 to 5.", result);
    }

    @Test
    public void testViewAverageRatings() {
        MovieRatingSystem.addMovie("Inception");
        MovieRatingSystem.rateMovie("Inception", 5.0);
        MovieRatingSystem.rateMovie("Inception", 4.0);

        String expected = "Average Ratings:\nInception: 4.5";
        String actual = MovieRatingSystem.viewAverageRatings();

        assertEquals(expected, actual);
    }
}
