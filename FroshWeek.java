public class FroshWeek {
    private static long inversions;

    private static void mergeSort(int[] a, int i, int j) {
        if (i < j) {
            int mid = (i + j) / 2;
            mergeSort(a, i, mid);
            mergeSort(a, mid + 1, j);
            merge(a, i, mid, j);
        }
    }

    private static void merge(int[] a, int i, int mid, int j) {
        int[] temp = new int[j - i + 1];
        int left = i, right = mid + 1, it = 0;
        while (left <= mid && right <= j) {
            if (a[left] <= a[right]) {
                temp[it++] = a[left++];
            } else {
                temp[it++] = a[right++];
                inversions += mid - left + 1;
            }
        }
        while (left <= mid) temp[it++] = a[left++];
        while (right <= j) temp[it++] = a[right++];
        for (int k = 0; k < temp.length; k++) {
            a[i + k] = temp[k];
        }
    }

    public static void main(String[] args) {
        Kattio io = new Kattio(System.in);
        int n = io.getInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = io.getInt();
        }
        mergeSort(a, 0, n - 1);
        System.out.println(inversions);
    }
}
