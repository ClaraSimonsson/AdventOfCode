import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

class Main {
    
    public static void main (String[] args) {
        List<Integer> nbrs = sortDocument();
        int counts = countIncreases(nbrs);
        System.out.println(counts);
    }

    /**
     * 
     */
    public static List<Integer> sortDocument(){
        BufferedReader in = null;
        FileReader fr = null;
        List<Integer> nr_list = new ArrayList<Integer>();

        try {
            fr = new FileReader("measures.txt");
            in = new BufferedReader(fr);
            String str;
            while ((str = in.readLine()) != null) {
                nr_list.add(Integer.parseInt(str));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return nr_list;
    } 

    public static Integer countIncreases(List<Integer> nmbrs){
        Integer count = 0;
        Integer last_nmb = nmbrs.get(0);
        for(int i = 1; i < nmbrs.size(); i++){
            int curr_nr = nmbrs.get(i);
            if(curr_nr > last_nmb){
                count++;
            }
            last_nmb = curr_nr;
        }
        return count;
    } 
}    