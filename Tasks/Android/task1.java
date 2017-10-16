// version 1.0
// powered off, write a simplest one, without any algorithm
// I will imporve it
import java.util.Scanner;


public class task1{
	public static void main(String []args)
	{
		Scanner sc = new Scanner(System.in);
		System.out.printf("Please enter the lenth of initial array: ");
		int n = sc.nextInt();
		int []a = new int[1000005];
		int []b = new int[1000005];
		for(int i = 0; i < n; i++)
			a[i] = sc.nextInt();
		System.out.println("Switch your operation:");
		System.out.println("1.insert a number into array.");
		System.out.println("  Input: 1 [position] [number]");
		System.out.println("2.find a number in array.");
		System.out.println("  Input: 2 [number]");
		System.out.println("3.find a sub-seq of the array.");
		System.out.println("  Input: 3 [lenth of sub-seq] [sub-seq]");
		System.out.println("4.sort the array.");
		System.out.println("  Input: 4");
		System.out.println("5.print the array.");
		System.out.println("  Input: 5");
		System.out.println("6.shutdown the process.");
		System.out.println("  Input: 6");
		boolean continuing = true;
		while(continuing)
		{
			int cmd = sc.nextInt();
			switch(cmd)
			{
				case 1:
					//could improve: splay?
					int pos = sc.nextInt();
					int num = sc.nextInt();
					if(pos >= n) pos = n;
					for(int i = n++; i > pos; i--) 
						a[i] = a[i-1];
					a[pos] = num;
					break;
				case 2:
					int _nu = sc.nextInt(), tmp = 0;
					System.out.printf("{");
					for(int i : a) if(i == _nu) tmp++;
					for(int i = 0; i < n; i++) if(a[i] == _nu)
					{
						System.out.printf("%d", i);
						if((--tmp) > 0) System.out.printf(", ");
					}
					System.out.printf("}\n");
					break;
				case 3:
					//could improve: KMP
					boolean failed = true;
					int lenb = sc.nextInt();
					for(int i = 0; i < lenb; i++)
						b[i] = sc.nextInt();
					for(int i = 0; i <= n-lenb; i++)
					{
						boolean flag = true;
						for(int j = 0; j < lenb; j++)
						if(a[i+j] != b[j]) 
						{
							flag = false;
							break;
						}
						if(flag)
						{
							System.out.printf("%d\n",i);
							failed = false;
							break;
						}
					}
					if(failed) System.out.println("-1");
					break;
				case 4:
					//could improve merge sort
					for(int i = 0; i < n-1; i++)
					for(int j = i+1; j < n; j++)
					if(a[i] > a[j])
					{
						int _tmp = a[j];
						a[j] = a[i];
						a[i] = _tmp;
					}
					break;
				case 5:
					System.out.printf("{");
					for(int i = 0; i < n-1; i++)
						System.out.printf("%d, ", a[i]);
					System.out.printf("%d}\n", a[n-1]);
					break;
				case 6:
					continuing = false;
					break;
				default:
					System.out.println("Invalid input!");
			}
		}
	}
}
