import java.util.HashMap;
import java.util.Map;

public class Bokforing {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in);
        int n = io.getInt();
        int q = io.getInt();
        Map<Integer, Integer> map = new HashMap<>();
        int x = 0;
        while (q-- > 0) {
            switch (io.getWord()) {
                case "SET":
                    map.put(io.getInt(), io.getInt());
                    break;
                case "RESTART":
                    x = io.getInt();
                    map = new HashMap<>();
                    break;
                default:
                    io.println(map.getOrDefault(io.getInt(), x));
                    break;
            }
        }
        io.close();
    }
}
