# mcds.make_graph_gml()


## input:
```
            graph_type: string; default is neighbor
                to specify which physicell output data should be processed.
                attached: processes mcds.get_attached_graph_dict dictionary.
                neighbor: processes mcds.get_neighbor_graph_dict dictionary.

            edge_attr: boolean; default True
                specifies if the spatial Euclidean distance is used for
                edge attribute, to generate a weighted graph.

            node_attr: list of strings; default is empty list
                list of mcds.get_cell_df dataframe columns, used for
                node attributes.

```

## output:
```
            gml file, generated under the returned path.

```

## description:
```
            function to generate graph files in the gml graph modelling language
            standard format.

            gml was the outcome of an initiative that started at
            the international symposium on graph drawing 1995 in Passau
            and ended at Graph Drawing 1996 in Berkeley. the networkx python
            and igraph C and python libraries for graph analysis are
            gml compatible and can as such read and write this file format.

            https://en.wikipedia.org/wiki/Graph_Modelling_Language
            https://networkx.org/
            https://igraph.org/
        
```