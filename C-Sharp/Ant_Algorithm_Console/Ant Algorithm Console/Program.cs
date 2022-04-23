using System;

namespace Ant_Algorithm_Console
{
    class Program
    {



        static void Main(string[] args)
        {

            
            int Num_of_vertex=50;
            int Num_of_ants=50;
            int Num_of_iterations=10;

            double Weight_constant=10;
            double Q_constant=10;

            double Weight_priority_factor=1;
            double Feromone_priority_factor=4;

            double Feromone_remain_precentage=0.1;
            double Default_feromone_value=0.1;
            double Default_delta_feromone = 0.01;

            AntAlgorithm_class alg = new AntAlgorithm_class(
                    Num_of_vertex,
                    Num_of_ants,
                    Num_of_iterations,
                    Weight_constant,
                    Q_constant,
                    Weight_priority_factor,
                    Feromone_priority_factor,
                    Feromone_remain_precentage,
                    Default_feromone_value,
                    Default_delta_feromone);

            alg.Set_graph_random(2);
            double total_len = 1111;
            int iter = 0;
            while (total_len > 1000)
            {
                if (iter % 100 == 0)
                {
                    alg.graph.Reset_feromone_add_amount();
                    alg.graph.Set_feromone_default_value(Default_feromone_value);
                }

                alg.Evaluate();

                System.Console.Clear();

                alg.Show_path();
                Console.WriteLine("\n--------------------------------------------------");
                //alg.Show_weight_matrix();
                //Console.WriteLine("--------------------------------------------------");
                //alg.Show_feromone_matrix();

                Console.WriteLine("\n\n==================================================");

                total_len = alg.total_length;
                Console.WriteLine($"iteration: {iter++} \ntotal length: {total_len}");

                //System.Threading.Thread.Sleep(500);
                
            }



            

           
        }



    }
}
