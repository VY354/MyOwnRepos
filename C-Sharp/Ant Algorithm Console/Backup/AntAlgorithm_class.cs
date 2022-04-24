using System;
using System.Collections.Generic;
using System.Text;

namespace Ant_Algorithm_Console
{

    public class ProbArrCompaper : IComparer<double[]>
    {
        int IComparer<double[]>.Compare(double[] x, double[] y)
        {
            return (x[1].CompareTo(y[1]));
        }
    }

    public class AntAlgorithm_class
    {
        public struct Ant
        {
            public int Start_vertex_index;
            public List<Path> Path;
        };
       
        // graph  properties
        private int Num_of_vertex;
        private VertexGraph Graph;

        // paths variables
        private double Default_feromone_value;
        private List<List<Path>> Walked_paths;
        private List<Path> Total_path;
        private double Total_length;

        // ants and iterations parameters
        private int Num_of_ants;
        private Ant[] Ants;
        private double Default_delta_feromone;

        // algorithm parameters
        private int Num_of_iterations;
        private double Weight_constant;
        private double Q_constant;
        private double Feromone_remain_precentage;

        // ants property orientation
        private double Weight_priority_factor;
        private double Feromone_priority_factor;

        public AntAlgorithm_class()
        {
            Num_of_vertex = 1;
            Graph = new VertexGraph(1);

            Default_feromone_value = 1;
            Walked_paths = new List<List<Path>>();
            Total_path = new List<Path>();
            Total_length = 0;

            Num_of_ants = 1;
            Ants = new Ant[1];
            Default_delta_feromone = 1;

            Num_of_iterations = 1;
            Weight_constant = 1;
            Q_constant = 1;
            Feromone_remain_precentage = 1;

            Weight_priority_factor = 1;
            Feromone_priority_factor = 1;
        }

        public AntAlgorithm_class(int num_of_vertex, 
            int num_of_ants, 
            int num_of_iterations, 
            double weight_constant, 
            double q_constant, 
            double weight_priority_factor, 
            double feromone_priority_factor,
            double feromone_remain_precentage, 
            double path_default_feromone, 
            double default_delta_feromone)
        {
            Num_of_vertex = num_of_vertex;
            Graph = new VertexGraph(Num_of_vertex);

            Default_feromone_value = path_default_feromone;
            Walked_paths = new List<List<Path>>();
            Total_path = new List<Path>();
            Total_length = -1;

            Num_of_ants = num_of_ants;
            Ants = new Ant[num_of_ants];
            Default_delta_feromone = default_delta_feromone;

            Num_of_iterations = num_of_iterations;
            Weight_constant = weight_constant;
            Q_constant = q_constant;
            Feromone_remain_precentage = feromone_remain_precentage;

            Weight_priority_factor = weight_priority_factor;
            Feromone_priority_factor = feromone_priority_factor;
        }

        public int num_of_vertex { get => Num_of_vertex; set => Num_of_vertex = value; }
        public VertexGraph graph { get => Graph; }

        public double path_default_feromone { get => Default_feromone_value; set => Default_feromone_value = value; }
        public List<Path> total_path { get => Total_path; }
        public double total_length { get => Total_length; }


        public int num_of_ants { get => Num_of_ants; set => Num_of_ants = value; }
        public double default_delta_feromone { get => Default_delta_feromone; set => Default_delta_feromone = value; }


        public int num_of_iterations { get => Num_of_iterations; set => Num_of_iterations = value; }
        public double weight_constant { get => Weight_constant; set => Weight_constant = value; }
        public double q_constant { get => Q_constant; set => Q_constant = value; }
        public double feromone_remain_precentage { get => Feromone_remain_precentage; set => Feromone_remain_precentage = value; }
      
        public double weight_priority_factor { get => Weight_priority_factor; set => Weight_priority_factor = value; }
        public double feromone_priority_factor { get => Feromone_priority_factor; set => Feromone_priority_factor = value; }


        public void Evaluate()
        {
            //Graph.Reset_feromone_add_amount();
            //Graph.Set_feromone_default_value(Default_feromone_value);

            // at each iteration
            for (int iteration = 0; iteration < Num_of_iterations; iteration++)
            {
                Random rnd = new Random();
                int start_vertex = rnd.Next() % Num_of_vertex;
                Walked_paths = new List<List<Path>>();
                
                // for each ant
                for (int antIndex = 0; antIndex < Num_of_ants; antIndex++)
                {
                    // create new ant
                    Ant ant = new Ant();
                    ant.Path = new List<Path>();
                    ant.Start_vertex_index = start_vertex;

                    // add new walked path
                    Walked_paths.Add(new List<Path>());

                    // for each vertex
                    for (int vertexIndex = 0; vertexIndex < Num_of_vertex ; vertexIndex++)
                    {
                        // calculate probabilities
                        double total_desire = Calculate_desirability_sum(ant);
                        List<double[]> probabilities = Calculate_probabilities(ant, total_desire);

                        // move to next vertex
                        int next_vertex = Pick_next_vertex(probabilities);
                        Path path_to_add = Graph.Paths[ant.Start_vertex_index, next_vertex];
                        ant.Path.Add(path_to_add);

                        /* accumulate feromone for distribution.
                         * As path matrix is simmetric, can update and add only one side of matrix
                        */
                        path_to_add.Feromone_amount_to_add += Default_delta_feromone;
                        Walked_paths[antIndex].Add(path_to_add);

                        ant.Start_vertex_index = next_vertex;
                    }
                }
                Distribute_feromone();
                Calculate_iteration_path_length();
            }
        }


        private double Calculate_probability(Vertex2D from, Vertex2D to, double total_desire)
        {
            double desire = Calculate_desirability(from, to);
            return desire / total_desire;
        }

        private List<double[]> Calculate_probabilities(Ant ant, double total_desire)
        {
            List<double[]> probabilities;
            probabilities = new List<double[]>();

            // get ants last vertex and its index
            Vertex2D curr_vertex;
            if (ant.Path.Count == 0) curr_vertex = Graph.Verticies[ant.Start_vertex_index];
            else curr_vertex = ant.Path[ant.Path.Count - 1].connection.vertex_2;
            int curr_index = curr_vertex.index;

            foreach (Vertex2D vertex in curr_vertex.connected_verticies)
            {
                // skip visited verticies
                if (ant.Path.Exists(v => v.connection.vertex_1 == vertex)) continue;

                double prob = Calculate_probability(curr_vertex, vertex, total_desire);
                probabilities.Add(new double[2] { vertex.index, prob });
            }

            // if there is no unvisited verticies go to begin of path
            if (probabilities.Count == 0)
                probabilities.Add(new double[2] { ant.Path[0].connection.vertex_1.index, 1 });

            return probabilities;
        }

        private double Calculate_desirability(Vertex2D from, Vertex2D to)
        {
            // pick path
            Path path = Graph.Paths[from.index, to.index];
            double weight_normalized = Weight_constant / path.connection.weight;

            // powering to priorities factors
            double feromone_value_powered = Math.Pow(path.Feromone_value, Feromone_priority_factor);
            double weight_normalized_value_powered = Math.Pow(weight_normalized, Weight_priority_factor);

            double desire = feromone_value_powered * weight_normalized_value_powered;

            return desire;
        }

        private double Calculate_desirability_sum(Ant ant)
        {
            double total_desire = 0;

            // get ants last vertex
            Vertex2D curr_vertex;
            if (ant.Path.Count == 0) curr_vertex = Graph.Verticies[ant.Start_vertex_index];
            else curr_vertex = ant.Path[ant.Path.Count - 1].connection.vertex_2;

            foreach(Vertex2D vertex in curr_vertex.connected_verticies)
            {
                // skip visited verticies
                if (ant.Path.Exists(v => v.connection.vertex_1 == vertex)) continue;

                double desire = Calculate_desirability(curr_vertex, vertex);
                total_desire += desire;
            }

            if (total_desire == 0) return 1;
            return total_desire;
        }

        private int Pick_next_vertex(List<double[]> probabilities)
        {
            // if have only one vertex to go
            if (probabilities.Count == 1)
            {
                return Convert.ToInt32(probabilities[0][0]);
            }

            Random random = new Random();
            double rand_val = random.NextDouble();

            probabilities.Sort(new ProbArrCompaper());

            double curr_space = 0;
            int i = 0;
            for (i = 0; i < probabilities.Count; i++)
            {
                curr_space += probabilities[i][1];
                if (rand_val < curr_space) 
                    return Convert.ToInt32(probabilities[i][0]);
            }

            // if last section
            return Convert.ToInt32(probabilities[i - 1][0]);
        }

        private void Distribute_feromone()
        {

            for (int i = 0; i < Walked_paths.Count; i++)
            {
                for (int j = 0; j < Walked_paths[i].Count; j++)
                {
                    Path path = Walked_paths[i][j];
                    double feromone_amount_to_add = path.Feromone_amount_to_add;
                    path.Feromone_value *= feromone_remain_precentage;
                    path.Feromone_value += feromone_amount_to_add;

                    Graph.Paths[path.connection.vertex_1.index, path.connection.vertex_2.index] = path;
                }
            }
        }

        private void Calculate_iteration_path_length()
        {
            double total_length = 0;
            List<Path> total_path = new List<Path>();

            // go trough path matrix and pick path with max feromone value
            int next_ind = -1;
            int jump_count = 0;

            int i = 0;
            int j = 0;
            for (i = 0; jump_count<Num_of_vertex;)
            {
                // find max feromone path
                double max_feromone = 0;
                for (j = 0; j < Num_of_vertex; j++)
                {
                    if (Graph.Paths[i, j].Feromone_value > max_feromone
                        && (total_path.Exists(path => path.connection.vertex_1 == Graph.Paths[i, j].connection.vertex_2) == false
                        ))
                    {
                        max_feromone = Graph.Paths[i, j].Feromone_value;
                        next_ind = j;
                    }
                }
                if(i == next_ind) total_path.Add(Graph.Paths[next_ind, 0]);
                else total_path.Add(Graph.Paths[i, next_ind]);

                // jump to next vertex (matrix line)
                i = next_ind;
                jump_count++;
            }
            
            // sum paths weights
            foreach (Path path in total_path)
            {
                total_length += path.connection.weight;
            }

            if (Total_length > total_length || Total_length == -1)
            {
                Total_length = total_length;
                Total_path = new List<Path>();
                foreach (Path path in total_path)
                {
                    Total_path.Add(path);
                }
            }
        }



        public void Set_feromone_default()
        {
            graph.Reset_feromone_add_amount();
            graph.Set_feromone_default_value(Default_feromone_value);
        }

        public void Set_graph_random(int tens_factor=2)
        {
            Graph.Set_verticies_random(tens_factor);
            Graph.Set_weights_random(tens_factor);
            Graph.Initialize_graph();
            Graph.Set_feromone_default_value(Default_feromone_value);
        }

        public void Set_verticies_from()
        {
            


        }


        public void Show_path()
        {
            Console.WriteLine($"Total path weight: {Total_length}");
            Console.WriteLine("================================");
            Console.Write("Path: ");
            Console.Write($"{Total_path[0].connection.vertex_1.index}" + "  ");
            foreach (Path path in Total_path)
            {
                Console.Write($"{path.connection.vertex_2.index}" + "  ");
            }
        }

        public void Show_weight_matrix()
        {
            for (int i = 0; i < Num_of_vertex; i++)
            {
                for (int j = 0; j < i; j++)
                {
                    Console.Write(String.Format("{0:n2}  ", Graph.Paths[i, j].connection.weight));
                }
                Console.Write("\n");
            }
        }

        public void Show_feromone_matrix()
        {
            for (int i = 0; i < Num_of_vertex; i++)
            {
                for (int j = 0; j < Num_of_vertex; j++)
                {
                    Console.ResetColor();
                    if (Total_path.Exists(p => p == Graph.Paths[i, j]))
                    {
                        Console.BackgroundColor = ConsoleColor.Gray;
                        Console.ForegroundColor = ConsoleColor.Black;
                    }
                    else
                    {
                        Console.BackgroundColor = ConsoleColor.Black;
                        Console.ForegroundColor = ConsoleColor.Gray;
                    }
                    Console.Write(String.Format("{0,10:f3} ", Graph.Paths[i, j].Feromone_value));
                }
                Console.Write("\n");
            }
        }


    }
}
