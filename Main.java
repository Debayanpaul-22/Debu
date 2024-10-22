//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
import java.util.Scanner;
class BankApp{
    String account;
    String name;
    String acc_type;
    Long balance;
    Scanner sc=new Scanner(System.in);

    public void newAccount(){
        System.out.print("Enter Account number: ");
        account=sc.next();
        System.out.print("Enter Account type: ");
        acc_type=sc.next();
        System.out.print("Enter Name: ");
        name=sc.next();
        System.out.print("Enter Balance: ");
        balance=sc.nextLong();
    }

    public void showAccount(){
        System.out.println("Account number is "+account);
        System.out.println("Account type is "+acc_type);
        System.out.println("Name of account holder is "+name);
        System.out.println("Account balance is "+balance);
    }

    public void deposit(){
        Integer dpo;
        System.out.print("Enter Amount you want to deposit: ");
        dpo=sc.nextInt();
        balance=balance+dpo;
    }

    public void withdraw(){
        Integer widr;
        System.out.print("Enter Amount you want to withdraw: ");
        widr=sc.nextInt();
        if(balance<widr){
            System.out.print("Your balance is less than "+widr+" !!!Transition fails");
        }
        else {
            balance=balance-widr;
        }
        
    }
    public boolean search(String ac_no) {

        if (account.equals(ac_no)) {
            showAccount();
            return (true);
        }
        return (false);
    }
}  


public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int num;
        System.out.print("How many number of customer you want to input: ");
        num=sc.nextInt();
        BankApp c[]=new BankApp[num];
        for(int i=0;i< c.length;i++){
            c[i]=new BankApp();
            c[i].newAccount();
        }

            int ch = 0;
            System.out.println(" 1. Display all account details \n 2. Search by Account number\n 3. Deposit the amount \n 4. Withdraw the amount \n 5.Exit");
            ch=sc.nextInt();
            switch (ch) {
                case 1:
                    for (int i = 0; i < c.length; i++) {
                        c[i].showAccount();
                        break;
                    }
                case 2:
                    String acc;
                    System.out.print("Enter account number that you want to search: ");
                    acc = sc.next();
                    boolean found = false;
                    for (int i = 0; i < c.length; i++) {
                        found = c[i].search(acc);
                        if (!found) {
                            System.out.print("!!Searching fail !!! Account doesn't exist");
                            break;
                        }
                    }
                    break;
                case 3:
                    String acc1;
                    System.out.print("Enter account number: ");
                    acc1 = sc.next();
                    boolean found1 = false;
                    for (int i = 0; i < c.length; i++) {
                        found1 = c[i].search(acc1);
                        if (found1) {
                            c[i].deposit();
                        } else {
                            System.out.println("Account doesn't exist");
                        }
                    }
                    break;
                case 4:
                    String acc2;
                    System.out.print("Enter account number: ");
                    acc2 = sc.next();
                    boolean found2 = false;
                    for (int i = 0; i < c.length; i++) {
                        found2 = c[i].search(acc2);
                        if (found2) {
                            c[i].withdraw();
                        } else {
                            System.out.println("Account doesn't exist");
                        }
                    }
                    break;
                case 5:
                    System.out.print("See you soon");
                    break;
                default:
                    System.out.print("You enter wrong choice");

            }

    }
}