import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;


/**
 * *
 * A Source Line of Code (SLOC) counting tool.
 *
 * @author cdjaw
 * @version  0.1
 */
public class SlocCounter {

    public static String readFileAsString(String absolutFilePath) throws Exception {
        return new String(Files.readAllBytes(Paths.get(absolutFilePath)));
    }

    public static String removeBlockComments(String sourceFileContents) {
        return sourceFileContents.replaceAll("(?s)/\\*.*?\\*/", "");
    }

    public static boolean lineContainsSourceCode(String line) {
        String lineWithoutComments = line.replaceAll("//.*$", "");
        return lineWithoutComments.trim().length() > 0;
    }

    public static ArrayList<String> filterSourceLinesOfCode(String sourceFileContents) {
        ArrayList<String> sourceLinesOfCode;
        String[] remainingLinesOfCode;
        String remainingFileContents;

        remainingFileContents = removeBlockComments(sourceFileContents);
        remainingLinesOfCode = remainingFileContents.split("\n");
        sourceLinesOfCode = new ArrayList<>();

        for(String temp: remainingLinesOfCode) {
            if(lineContainsSourceCode(temp)) {
                sourceLinesOfCode.add(temp);
            }
        }
        return sourceLinesOfCode;
    }

    public static int countSourceLinesOfCode(String absoluteFilePath) throws Exception {
        String fileContents;
        ArrayList<String> sourceLinesOfCode;

        fileContents = readFileAsString(absoluteFilePath);
        sourceLinesOfCode = filterSourceLinesOfCode(fileContents);
        return sourceLinesOfCode.size();
    }

    public static void main(String[] args) {
        // TODO - add command line parser

        if(args.length != 1) {
            System.err.println("SlocCounter: error: requires exactly one parameter");
            System.out.println("SlocCounter: usage: java SlocCounter abs_file_path");
            System.exit(1);
        }

        try {
            System.out.println("SLOC:" + countSourceLinesOfCode(args[0]));
        } catch (Exception e) {
            System.err.println("SlocCounter: error: "+ e);
            System.exit(2);
        }
    }
}
