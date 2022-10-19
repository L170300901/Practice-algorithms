import java.io.*;
import java.util.*;

class Node{
   private int x;
   private int y;
   public Node(int x, int y){
      this.x = x;
      this.y = y;
   }
   
   public int getX(){
      return x;
   }
   public int getY(){
      return y;
   }

}

public class Main {

   public static void main(String[] args) throws IOException{
      // TODO Auto-generated method stub
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st = new StringTokenizer(br.readLine());
      int n = Integer.parseInt(st.nextToken());
      ArrayList<Node>list = new ArrayList<>();
      for(int i = 0 ; i < n ; i ++) {
         st = new StringTokenizer(br.readLine());
         int x = Integer.parseInt(st.nextToken());
         int y = Integer.parseInt(st.nextToken());
         list.add(new Node(x,y));
      }
      int sum = 0;
      for(int i = 0 ; i < list.size(); i++) {
         int x1 = list.get(i).getX();
         int y1 = list.get(i).getY();
         for(int j = i+1; j < list.size(); j++) {
            int x2 = list.get(j).getX();
            int y2 = list.get(j).getY();
            sum += Math.abs(x1 - x2) + Math.abs(y1 - y2); 
         }
      }
      System.out.println(sum);
   }

}