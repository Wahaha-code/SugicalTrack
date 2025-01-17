import numpy as np

class Ply:

    def __init__(self, points, colors):
        self.__points = points
        self.__colors = colors

    def write(self, filename):
        # Write the headers
        lines = self.__getLinesForHeader()

        fd = open(filename, "w")
        for line in lines:
            fd.write("%s\n" % line)

        # Write the points
        self.__writePoints(fd, self.__points, self.__colors)

        fd.close()

    def __getLinesForHeader(self):
        """
        Get the list of lines for the PLY header.
        """
        lines = [
            "ply",
            "format ascii 1.0",
            "comment generated by: kinectToPly",
            "element vertex %s" % len(self.__points),
            "property float x",
            "property float y",
            "property float z",
            "property uchar red",
            "property uchar green",
            "property uchar blue",
            "end_header",
            ]

        return lines

    def __writePoints(self, fd, points, colors):
        """
        Write the point cloud points to a file.
        fd -- The file descriptor
        points -- The matrix of points (num points, 3)
        colors -- The matrix of colors (num points, 3)
        """
        # Stack the two arrays together
        stacked = np.column_stack((points, colors))

        # Write the array to the file
        np.savetxt(
            fd,
            stacked,
            delimiter='\n',
            fmt="%f %f %f %d %d %d")
