    import java.util.Arrays;
    import java.util.Scanner;

    class ShellSort
    {
        
        public static int sort(int arr[])
        {
            int size = arr.length;
    
            for (int gap = size/2; gap > 0; gap /= 2)
            {

                for (int i = gap; i < size; i += 1)
                {

                    int temp = arr[i];
                    int j;
                    for (j = i; j >= gap && arr[j - gap] > temp; j -= gap)
                        arr[j] = arr[j - gap];
                    arr[j] = temp;
                }
            }
            return 0;
        }

        public static void main(String args[]){
            Scanner scan = new Scanner(System.in);
            int input,size;
            size = scan.nextInt();

            int [] array = new int[size];
            for (int i = 0; i < size; i++){
                input = scan.nextInt();
                array[i] = input;
            }
            float tinicio, tfinal, tiempo;

            tinicio = System.nanoTime();
            sort(array);
            tfinal = System.nanoTime();
            tiempo = tfinal -tinicio;
            System.out.print(tiempo/1000000000);


        }
    }
    