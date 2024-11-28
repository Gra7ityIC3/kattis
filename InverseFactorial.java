public class InverseFactorial {
    private static int solve(String s) {
        switch (s) {
            case "1": return 1;
            case "2": return 2;
            case "6": return 3;
            case "24": return 4;
            case "120": return 5;
            default:
                int n = 6;
                double L = Math.log10(720) + 1;
                while (L < s.length()) {
                    L += Math.log10(++n);
                }
                return n;
        }
    }

    public static void main(String[] args) {
        Kattio io = new Kattio(System.in);
        System.out.println(solve(io.getWord()));
    }
}
