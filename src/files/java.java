import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import java.io.FileOutputStream;
import com.itextpdf.text.DocumentException;
import com.itextpdf.text.Paragraph;
import com.itextpdf.text.pdf.PdfWriter;

// Main Class
public class JavaSampleApp {

    public static void main(String[] args) {
        // Multithreading Example
        ExecutorService executor = Executors.newFixedThreadPool(2);
        executor.submit(() -> printNumbers());
        executor.shutdown();

        // Database Operations
        System.out.println("Database Operations:");
        performDatabaseOperations();

        // API Consumption
        System.out.println("\nAPI Data:");
        fetchAPIData();

        // Web Scraping
        System.out.println("\nScraped Website Title:");
        scrapeWebsite();

        // PDF Generation
        System.out.println("\nPDF Creation:");
        createPDF();
    }

    // Multithreading Example
    public static void printNumbers() {
        for (int i = 1; i <= 5; i++) {
            System.out.println("Thread Number: " + i);
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    // Database Operations
    public static void performDatabaseOperations() {
        String url = "jdbc:sqlite:sample.db";

        try (Connection conn = DriverManager.getConnection(url)) {
            if (conn != null) {
                Statement stmt = conn.createStatement();
                // Create table
                stmt.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)");

                // Insert data
                PreparedStatement pstmt = conn.prepareStatement("INSERT INTO users (name, age) VALUES (?, ?)");
                pstmt.setString(1, "Alice");
                pstmt.setInt(2, 25);
                pstmt.executeUpdate();

                pstmt.setString(1, "Bob");
                pstmt.setInt(2, 30);
                pstmt.executeUpdate();

                // Retrieve data
                ResultSet rs = stmt.executeQuery("SELECT * FROM users");
                while (rs.next()) {
                    System.out.println("ID: " + rs.getInt("id") + ", Name: " + rs.getString("name") + ", Age: " + rs.getInt("age"));
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // API Consumption Example
    public static void fetchAPIData() {
        try {
            String apiUrl = "https://jsonplaceholder.typicode.com/posts/1";
            Document doc = Jsoup.connect(apiUrl).ignoreContentType(true).get();
            System.out.println(doc.text());
        } catch (Exception e) {
            System.out.println("Failed to fetch API data.");
        }
    }

    // Web Scraping Example
    public static void scrapeWebsite() {
        try {
            String url = "https://example.com";
            Document doc = Jsoup.connect(url).get();
            System.out.println(doc.title());
        } catch (Exception e) {
            System.out.println("Failed to scrape website.");
        }
    }

    // PDF Generation Example
    public static void createPDF() {
        String pdfPath = "sample.pdf";

        try {
            com.itextpdf.text.Document pdfDoc = new com.itextpdf.text.Document();
            PdfWriter.getInstance(pdfDoc, new FileOutputStream(pdfPath));
            pdfDoc.open();
            pdfDoc.add(new Paragraph("Hello, PDF!"));
            pdfDoc.close();
            System.out.println("PDF generated at " + pdfPath);
        } catch (DocumentException | java.io.IOException e) {
            System.out.println("Failed to create PDF.");
        }
    }
}
