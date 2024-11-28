import java.util.PriorityQueue;
import java.util.Queue;

public class CardTrading {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in);
        int n = io.getInt();
        int t = io.getInt();
        int k = io.getInt();
        int[] deck = new int[t + 1];
        for (int i = 0; i < n; i++) {
            deck[io.getInt()]++;
        }
        Queue<Integer> pq = new PriorityQueue<>(t);
        long profit = 0L;
        for (int i = 1; i <= t; i++) {
            int a = io.getInt();
            int b = io.getInt();
            pq.offer((2 - deck[i]) * a + deck[i] * b);
            profit += deck[i] * b;
        }
        for (int i = 0; i < k; i++) {
            profit -= pq.poll();
        }
        System.out.println(profit);
    }
}
