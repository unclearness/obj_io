import sys
import os
# To find obj_io
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import obj_io  # NOQA


def main():
    data_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', 'data'))
    names = ['spot_triangulated.obj', 'spot_quadrangulated.obj']
    for name in names:
        mesh = obj_io.loadObj(os.path.join(data_dir, name))
        mesh.recomputeNormals()
        out_dir = os.path.abspath(os.path.join(
            os.path.dirname(__file__), '..', 'out'))
        os.makedirs(out_dir, exist_ok=True)
        obj_io.saveObj(os.path.join(out_dir, name), mesh)


if __name__ == '__main__':
    main()
