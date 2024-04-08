import java.util.Scanner;
class Player{
    // Write the code for the Player class here.
    private int id;
    private String name;
    private String country;
    private int goals;
    
    public Player(int id, String name, String country, int goals){
        this.id = id;
        this.name = name;
        this.country = country;
        this.goals = goals;
    }
    
    public void setId(int id){
        this.id = id;
    }
    public int getId(){
        return id;
    }
    
    public void setName(String name){
        this.name = name;
    }
    public String getName(){
        return name;
    }
    
    public void setCountry(String country){
        this.country = country;
    }
    public String getCountry(){
        return country;
    }
    
    public void setGoals(int goals){
        this.goals = goals;
    }
    public int getGoals(){
        return goals;
    }
}

public class App {
    public static Player findPlayerWithMostGoals(Player[] players){
        
        // Enter the code for "findPlayerWithMostGoals" method here.
        if(players == null || players.length == 0)
            return null;
            
        Player maxGoalsPlayer = players[0];
        for(int i = 1; i<players.length; i++){
            if(players[i].getGoals() > maxGoalsPlayer.getGoals()){
                maxGoalsPlayer = players[i];
            }
        }
        return maxGoalsPlayer;
    } 
    public static void main(String args[]) throws Exception {
        
        // Enter your main code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        Player[] players = new Player[n];
        
        for(int i = 0; i<n; i++){
            int id = sc.nextInt();
            sc.nextLine();
            String name = sc.nextLine();
            String country = sc.nextLine();
            int goals = sc.nextInt();
            
            players[i] = new Player(id, name, country, goals);
        }
        
        Player playersWithMostGoals = findPlayerWithMostGoals(players);
        
        System.out.println(playersWithMostGoals.getId());
        System.out.println(playersWithMostGoals.getName());
        System.out.println(playersWithMostGoals.getCountry());
        System.out.println(playersWithMostGoals.getGoals());
    }
}
