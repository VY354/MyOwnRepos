using System;
using System.Collections.Generic;
using System.Text;

namespace Ant_Algorithm_Console
{
    public struct Vertex2D
    {
        public  int index;

        public double x;
        public double y;

        public List<Vertex2D> connected_verticies;

        public Vertex2D(int Index, double X, double Y)
        {
            index = Index;
            x = X;
            y = Y;
            connected_verticies = new List<Vertex2D>();
        }

        public static bool operator ==(Vertex2D v1, Vertex2D v2)
        {
            return (v1.x == v2.x && v1.y == v2.y);
        }

        public static bool operator !=(Vertex2D v1, Vertex2D v2)
        {
            return (v1.x != v2.x || v1.y != v2.y);
        }

    };

    public struct Connection
    {
        public Vertex2D vertex_1;
        public Vertex2D vertex_2;

        public double weight;

        public void Set_weight_as_length()
        {
            weight = Math.Sqrt(vertex_1.x * vertex_2.x + vertex_1.y * vertex_2.y);
        }

        public static bool operator ==(Connection c1, Connection c2)
        {
            return (c1.vertex_1 == c2.vertex_1 && c1.vertex_2 == c2.vertex_2);
        }

        public static bool operator !=(Connection c1, Connection c2)
        {
            return (c1.vertex_1 != c2.vertex_1 || c1.vertex_2 != c2.vertex_2);
        }

    };

    public struct Path
    {
        public Connection connection;

        public double Feromone_value;
        public double Feromone_amount_to_add;

        public Path(Vertex2D vertex1, Vertex2D vertex2, double Weight)
        {
            connection = new Connection();
            connection.weight = Weight;
            connection.vertex_1 = vertex1;
            connection.vertex_2 = vertex2;

            Feromone_value = 0;
            Feromone_amount_to_add = 0;
        }

        public static bool operator ==(Path path1, Path path2)
        {
            return (path1.connection.vertex_1 == path2.connection.vertex_1
                && path1.connection.vertex_2 == path2.connection.vertex_2);
        }

        public static bool operator !=(Path path1, Path path2)
        {
            return (path1.connection.vertex_1 != path2.connection.vertex_1
                || path1.connection.vertex_2 != path2.connection.vertex_2);
        }

    };


    public class VertexGraph
    {
        private int num_of_vertex;

        private double[,] weights;
        private Vertex2D[] verticies;
        private Path[,] paths;

        public int Num_of_vertex { get => num_of_vertex; set => num_of_vertex = value; }
        public double[,] Weights { get => weights; set => weights = value; }
        public Path[,] Paths { get => paths; }
        public Vertex2D[] Verticies { get => verticies; set => verticies = value; }

        VertexGraph()
        {
            num_of_vertex = 0;

            weights = new double[num_of_vertex, num_of_vertex];
            verticies = new Vertex2D[num_of_vertex];
            paths = new Path[num_of_vertex, num_of_vertex];
        }

        public VertexGraph(int Num_of_vertex)
        {
            num_of_vertex = Num_of_vertex;

            weights = new double[num_of_vertex, num_of_vertex];
            verticies = new Vertex2D[num_of_vertex];
            paths = new Path[num_of_vertex, num_of_vertex];
        }


        public void Initialize_graph()
        {
            for (int i = 0; i < Num_of_vertex; i++)
            {
                for (int j = 0; j < i; j++)
                {
                    paths[i, j] = new Path(verticies[i], verticies[j], weights[i, j]);
                    paths[j, i] = new Path(verticies[j], verticies[i], weights[j, i]);
                }
                paths[i, i] = new Path(verticies[i], verticies[i], weights[i, i]);
            }
        }


        public void Set_feromone_default_value(double default_feromone_value)
        {
            for (int i = 0; i < Num_of_vertex; i++)
            {
                for (int j = 0; j < i; j++)
                {
                    paths[i, j].Feromone_value = default_feromone_value;
                    paths[j, i].Feromone_value = default_feromone_value;
                }
                paths[i, i].Feromone_value = 0;
            }
        }

        public void Reset_feromone_add_amount()
        {
            for (int i = 0; i < Num_of_vertex; i++)
            {
                for (int j = 0; j < i; j++)
                {
                    paths[i, j].Feromone_amount_to_add = 0;
                    paths[j, i].Feromone_amount_to_add = 0;
                }
                paths[i, i].Feromone_amount_to_add = 0;
            }
        }

        public void Set_weights_random(int tens_factor = 2)
        {
            Random rnd = new Random();
            double up_border = Math.Pow(10, tens_factor);

            for (int i = 0; i < Num_of_vertex; i++)
            {
                for (int j = 0; j <= i; j++)
                {
                    double weight = rnd.Next() % up_border + 101;

                    weights[i, j] = weight;
                    weights[j, i] = weight;

                    if (i == j) weights[i, i] = 0;
                }
            }
        }

        public void Set_verticies_random(int tens_factor = 2)
        {
            Random rnd = new Random();
            double up_border = Math.Pow(10, tens_factor);

            for (int i = 0; i < Num_of_vertex; i++)
            {
                double x = rnd.Next() % up_border;
                double y = rnd.Next() % up_border;

                Vertex2D new_vertex = new Vertex2D(i, x, y);
                verticies[i] = new_vertex;

                for (int j = 0; j < i; j++)
                {
                    new_vertex.connected_verticies.Add(verticies[j]);
                    verticies[j].connected_verticies.Add(new_vertex);
                }
            }
        }



    }
}
