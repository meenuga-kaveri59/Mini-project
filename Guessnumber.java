import java.util.Random;
import java.util.Scanner;

class Guessnum {
    int computer;
    public Guessnum(){
        Random rand = new Random();
        computer = rand.nextInt(100);
        System.out.println("Guess the number from 1 to 100");
    }
    public int computerNo() { return computer;}
}
public class Guessnumber{
    static int takeUserInput(){
        int user;
        System.out.println("Enter ");
        Scanner sc = new Scanner(System.in);
        user=sc.nextInt();
        return user;
    }
    static void isCorrectNumber(int i,int j){
        if(i==j){
            System.out.println("Correct No. Guess");
        }
        else if(i>j){
            System.out.println("Your No. is Big than computer No.");
        }
        else{
            System.out.println("Your No. is Small than computer No.");
        }

    }
    public static void main(String[] args){
        int user=0,computer=0,iteration=0;
        Guessnum g = new Guessnum();
        do{
            user = takeUserInput();
            computer=g.computerNo();
//            System.out.println(user);
//            System.out.println(computer);
            isCorrectNumber(user,computer);
            iteration++;
        }while (user!=computer);
        System.out.println("YOU GUESS NO IN "+iteration+"ITERATIONS");
        

//      Create a class game , which allows a user to play"Guess The Number" game once.
//      Game should have the following methods:
//      Constructor to generate the random number
//      takesUserInput() to take a user input of number
//      isCorrectNumber()TO DETECT THE NUMBER ENTERED BY THE USER IS TRUE
//      GETTER AND SETTER FOR NOOFGUESSES
//      Use properties such as noofGuesses(int) ,etc to ger this task done

    }
    
}
