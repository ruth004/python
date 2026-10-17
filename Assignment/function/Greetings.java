import java.util.Scanner;

	public class Greetings{
	public static void main(String [] args){
	
	Scanner input = new Scanner(System.in);
	System.out.println("Enter name");
	String name = input.nextLine();
	
	System.out.println("Enter age");
	int age = input.nextInt();
	
	System.out.println("My name is :" + name);
	System.out.println("My age is :" +  age  + "year");
	}
	}
