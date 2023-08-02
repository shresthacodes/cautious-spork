import java.util.Random;
import java.util.Scanner;

public class quicksort {

    private int[] arr;

    public quicksort(int n) {
        arr = new int[n];
    }

    public void swap(int a, int b) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }

    public int partition(int low, int high) {
        int i = low + 1, j = high, key = arr[low];
        while (i <= j) {
            while (i <= j && key >= arr[i])
                i++;
            while (i <= j && key <= arr[j])
                j--;
            if (i < j)
                swap(i, j);
        }
        swap(low, j);
        return j;
    }

    public void qsort(int low, int high) {
        int s;
        if (low < high) {
            s = partition(low, high);
            qsort(low, s - 1);
            qsort(s + 1, high);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter choice : ");
        int choice = sc.nextInt();
        System.out.println("Enter length : ");
        int n = sc.nextInt();
        quicksort ob = new quicksort(n);
        if (choice == 1) {
            for (int i = 0; i < n; i++)
                ob.arr[i] = i;
        } else if (choice == 2) {
            for (int i = 0; i < n; i++)
                ob.arr[i] = n - i;
        } else {
            Random r = new Random();
            for (int i = 0; i < n; i++) {
                ob.arr[i] = r.nextInt(1000000);
            }
        }
        // QuickSort
        double st = System.nanoTime();
        ob.qsort(0, n - 1);
        double end = System.nanoTime();

        double time = end - st;
        time = time / (Math.pow(10, 6));
        System.out.println("\nTime taken : " + time);
        for (int i = 0; i < n; i++) {
            System.out.println(ob.arr[i]);
        }
        sc.close();
    }
}
