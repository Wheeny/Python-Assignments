import java.util.ArrayList;
import java.util.Scanner;

public class MovieRatingSystem {


    public static ArrayList<String> movies = new ArrayList<>();
    public static ArrayList<ArrayList<Double>> ratings = new ArrayList<>();

    public static String addMovie(String movieName) {
        if (movies.contains(movieName)) {
            return "Movie '" + movieName + "' already exists!";
        }

        movies.add(movieName);
        ratings.add(new ArrayList<Double>()); 
        return "Movie '" + movieName + "' added!";
    }

    public static String rateMovie(String movieName, double score) {
        if (!movies.contains(movieName)) {
            return "Movie '" + movieName + "' not found!";
        }

        if (score < 1 || score > 5) {
            return "Invalid rating! Enter a number from 1 to 5.";
        }

        int index = movies.indexOf(movieName);
        ratings.get(index).add(score);
        return "Rating added for '" + movieName + "' " + score;
    }

    public static String viewAverageRatings() {
        if (movies.isEmpty()) {
            return "No movies added yet.";
        }

        String output = "Average Ratings:\n";

        for (int i = 0; i < movies.size(); i++) {
            String name = movies.get(i);
            ArrayList<Double> movieRatings = ratings.get(i);

            if (!movieRatings.isEmpty()) {
                double sum = 0;
                for (double rating : movieRatings) {
                    sum += rating;
                }
                double average = sum / movieRatings.size();
                output += name + ": " + average + "\n";
            } else {
                output += name + ": No ratings yet\n";
            }
        }

        return output.trim();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n1. Add a Movie");
            System.out.println("2. Rate a Movie");
            System.out.println("3. View Average Ratings");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");

            String choice = scanner.nextLine();

            if (choice.equals("1")) {
                System.out.print("Enter the movie name: ");
                String name = scanner.nextLine();
                System.out.println(addMovie(name));

            } else if (choice.equals("2")) {
                System.out.print("Enter the movie name: ");
                String name = scanner.nextLine();
                System.out.print("Enter your rating (1-5): ");
                double score = Double.parseDouble(scanner.nextLine());
                System.out.println(rateMovie(name, score));

            } else if (choice.equals("3")) {
                System.out.println(viewAverageRatings());

            } else if (choice.equals("4")) {
                System.out.println("Exiting the application. Goodbye!");
                break;

            } else {
                System.out.println("Invalid choice, try again.");
            }
        }

        scanner.close();
    }
}
