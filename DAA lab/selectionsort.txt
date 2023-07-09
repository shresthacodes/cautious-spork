import java.util.Random;
import java.util.Scanner;

class ssort {
    int n;
    int arr[];

    // Create an array with random numbers
    // User specifies the number of array elements.
    public void create_array(int n, int choice) {
        // choice = 0 for elements already in sorted order
        // choice = 1 for elements already in sorted in reverse order
        // choice = 2 for random elements
        this.n = n;
        arr = new int[n];
        if (choice == 0) {
            for (int i = 0; i < n; i++)
                arr[i] = i;
        } else if (choice == 1) {
            for (int i = 0; i < n; i++)
                arr[i] = n - i;
        } else {
            Random rand = new Random();
            // Store the array with random numbers with values between 1 and 1,000,000
            for (int i = 0; i < n; i++)
                arr[i] = rand.nextInt(1000000);
        }
    }

    // Selection sort
    public void sort() {
        // Write your own Logic of Selection sort
    }

    // Swap function to swap two array elements.
    // Indices of the two array elements are parameters
    private void swap(int arr[], int i, int j) {
        int temp;
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public void print_array() {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println("\n");
    }
}

public class Selectionsort {
public static void main(String[] args) {
		
		ssort sort_obj=new ssort();
		int n;
		long start,end,time;
		
		//Create an array with random numbers or sorted numbers
		Scanner sobj=new Scanner(System.in);
		System.out.println("Enter the no. of elements to be created :");
		n=sobj.nextInt();
		sort_obj.create_array(n,2);
		System.out.println("Array elements to be sorted are :");
		sort_obj.print_array();
		
		// Run selection sort algorithm.
		// Measure system time before sorting starts and after sorting ends.		
		start=System.nanoTime(); // System.currentTimeMillis() gives milliseconds
		sort_obj.sort();
		end=System.nanoTime();
		System.out.println("\nThe sorted elements are :");
		sort_obj.print_array();
		time = (end-start)/1000000L;
		System.out.println("\nThe time taken to sort " + n + " elements is "+time+"ms");