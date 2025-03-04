#####
# title: test_snapshot_2d.py
#
# language: python3
# author: Elmar Bucher
# date: 2022-10-15
# license: BSD 3-Clause
#
# description:
#   pytest unit test library for the pcdl library pyMCDS class.
#   + https://docs.pytest.org/
#
#   note:
#   assert actual == expected, message
#   == value equality
#   is reference equality
#   pytest.approx for real values
#####


# load library
import matplotlib.pyplot as plt
import numpy as np
import os
import pathlib
import pcdl


# const
s_path_2d = str(pathlib.Path(pcdl.__file__).parent.resolve()/'data_timeseries_2d')
s_file_2d = 'output00000024.xml'
s_pathfile_2d = f'{s_path_2d}/{s_file_2d}'


## download test dataset ##
if not os.path.exists(s_path_2d):
    pcdl.install_data()


## data loading related functions ##

class TestPyMcdsInit(object):
    ''' tests for loading a pcdl.pyMCDS data set. '''
    mcds = pcdl.pyMCDS(xmlfile=s_file_2d, output_path=s_path_2d, custom_type={}, microenv=True, graph=True, settingxml='PhysiCell_settings.xml', verbose=True)
    df_cell = mcds.get_cell_df()
    def test_mcds_init_microenv(self, mcds=mcds, df_cell=df_cell):
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_cell)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (df_cell.shape == (1099, 95))

    def test_mcds_init_graph(self, mcds=mcds):
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(mcds.data['discrete_cells']['graph']['attached_cells'])) == "<class 'dict'>") and \
              (str(type(mcds.data['discrete_cells']['graph']['neighbor_cells'])) == "<class 'dict'>") and \
              (len(mcds.data['discrete_cells']['graph']['attached_cells']) == 1099) and \
              (len(mcds.data['discrete_cells']['graph']['neighbor_cells']) == 1099)

    def test_mcds_init_settingxml(self, mcds=mcds, df_cell=df_cell):
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_cell)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (set(df_cell.columns).issuperset({'cancer_cell_attack_rates'})) and \
              (df_cell.shape == (1099, 95))


class TestPyMcdsInitMicroenvFalse(object):
    ''' tests for loading a pcdl.pyMCDS data set with microenv false. '''
    mcds = pcdl.pyMCDS(xmlfile=s_file_2d, output_path=s_path_2d, custom_type={}, microenv=False, graph=True, settingxml='PhysiCell_settings.xml', verbose=True)
    df_cell = mcds.get_cell_df()
    def test_mcds_init_microenv(self, mcds=mcds, df_cell=df_cell):
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_cell)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (df_cell.shape == (1099, 92))

    def test_mcds_init_graph(self, mcds=mcds):
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(mcds.data['discrete_cells']['graph']['attached_cells'])) == "<class 'dict'>") and \
              (str(type(mcds.data['discrete_cells']['graph']['neighbor_cells'])) == "<class 'dict'>") and \
              (len(mcds.data['discrete_cells']['graph']['attached_cells']) == 1099) and \
              (len(mcds.data['discrete_cells']['graph']['neighbor_cells']) == 1099)

    def test_mcds_init_settingxml(self, mcds=mcds, df_cell=df_cell):
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_cell)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (set(df_cell.columns).issuperset({'cancer_cell_attack_rates'})) and \
              (df_cell.shape == (1099, 92))


class TestPyMcdsInitGraphFalse(object):
    ''' tests for loading a pcdl.pyMCDS data set with graph false. '''
    mcds = pcdl.pyMCDS(xmlfile=s_file_2d, output_path=s_path_2d, custom_type={}, microenv=True, graph=False, settingxml='PhysiCell_settings.xml', verbose=True)
    df_cell = mcds.get_cell_df()
    def test_mcds_init_microenv(self, mcds=mcds, df_cell=df_cell):
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_cell)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (df_cell.shape == (1099, 95))

    def test_mcds_init_graph(self, mcds=mcds):
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(mcds.data['discrete_cells']['graph']['attached_cells'])) == "<class 'dict'>") and \
              (str(type(mcds.data['discrete_cells']['graph']['neighbor_cells'])) == "<class 'dict'>") and \
              (len(mcds.data['discrete_cells']['graph']['attached_cells']) == 0) and \
              (len(mcds.data['discrete_cells']['graph']['neighbor_cells']) == 0)

    def test_mcds_init_settingxml(self, mcds=mcds, df_cell=df_cell):
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_cell)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (set(df_cell.columns).issuperset({'cancer_cell_attack_rates'})) and \
              (df_cell.shape == (1099, 95))


class TestPyMcdsInitSettingxmlFalse(object):
    ''' tests for loading a pcdl.pyMCDS data set with settingxml false. '''
    mcds = pcdl.pyMCDS(xmlfile=s_file_2d, output_path=s_path_2d, custom_type={}, microenv=True, graph=True, settingxml=False, verbose=True)
    df_cell = mcds.get_cell_df()
    def test_mcds_init_microenv(self, mcds=mcds, df_cell=df_cell):
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_cell)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (df_cell.shape == (1099, 95))

    def test_mcds_init_graph(self, mcds=mcds):
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(mcds.data['discrete_cells']['graph']['attached_cells'])) == "<class 'dict'>") and \
              (str(type(mcds.data['discrete_cells']['graph']['neighbor_cells'])) == "<class 'dict'>") and \
              (len(mcds.data['discrete_cells']['graph']['attached_cells']) == 1099) and \
              (len(mcds.data['discrete_cells']['graph']['neighbor_cells']) == 1099)

    def test_mcds_init_settingxml(self, mcds=mcds, df_cell=df_cell):
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_cell)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (set(df_cell.columns).issuperset({'attack_rates_0'})) and \
              (df_cell.shape == (1099, 95))


class TestPyMcdsInitSettingxmlNone(object):
    ''' tests for loading a pcdl.pyMCDS data set with settingxml none. '''
    mcds = pcdl.pyMCDS(xmlfile=s_file_2d, output_path=s_path_2d, custom_type={}, microenv=True, graph=True, settingxml=None, verbose=True)
    df_cell = mcds.get_cell_df()
    def test_mcds_init_microenv(self, mcds=mcds, df_cell=df_cell):
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_cell)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (df_cell.shape == (1099, 95))

    def test_mcds_init_graph(self, mcds=mcds):
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(mcds.data['discrete_cells']['graph']['attached_cells'])) == "<class 'dict'>") and \
              (str(type(mcds.data['discrete_cells']['graph']['neighbor_cells'])) == "<class 'dict'>") and \
              (len(mcds.data['discrete_cells']['graph']['attached_cells']) == 1099) and \
              (len(mcds.data['discrete_cells']['graph']['neighbor_cells']) == 1099)

    def test_mcds_init_settingxml(self, mcds=mcds, df_cell=df_cell):
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_cell)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (set(df_cell.columns).issuperset({'attack_rates_0'})) and \
              (df_cell.shape == (1099, 95))


class TestPyMcdsInitVerboseTrue(object):
    ''' tests for loading a pcdl.pyMCDS data set and set_verbose_false function. '''
    mcds = pcdl.pyMCDS(xmlfile=s_file_2d, output_path=s_path_2d, custom_type={}, microenv=True, graph=True, settingxml='PhysiCell_settings.xml', verbose=True)

    def test_mcds_verbose_true(self, mcds=mcds):
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (mcds.verbose)

    def test_mcds_set_verbose_false(self, mcds=mcds):
        mcds.set_verbose_false()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (not mcds.verbose)


class TestPyMcdsInitVerboseFalse(object):
    ''' tests for loading a pcdl.pyMCDS data set and set_verbose_true function. '''
    mcds = pcdl.pyMCDS(xmlfile=s_file_2d, output_path=s_path_2d, custom_type={}, microenv=True, graph=True, settingxml='PhysiCell_settings.xml', verbose=False)

    def test_mcds_verbose_false(self, mcds=mcds):
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (not mcds.verbose)

    def test_mcds_set_verbose_true(self, mcds=mcds):
        mcds.set_verbose_true()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (mcds.verbose)


## metadata related functions ##

class TestPyMcdsMetadata(object):
    ''' tests for pcdl.pyMCDS metadata related functions. '''
    mcds = pcdl.pyMCDS(xmlfile=s_file_2d, output_path=s_path_2d, custom_type={}, microenv=True, graph=True, settingxml='PhysiCell_settings.xml', verbose=True)

    def test_mcds_get_multicellds_version(self, mcds=mcds):
        s_mcdsversion = mcds.get_multicellds_version()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(s_mcdsversion)) == "<class 'str'>") and \
              (s_mcdsversion == 'MultiCellDS_2')

    def test_mcds_get_physicell_version(self, mcds=mcds):
        s_pcversion = mcds.get_physicell_version()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(s_pcversion)) == "<class 'str'>") and \
              (s_pcversion == 'PhysiCell_1.10.4')

    def test_mcds_get_timestamp(self, mcds=mcds):
        s_timestamp = mcds.get_timestamp()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(s_timestamp)) == "<class 'str'>") and \
              (s_timestamp == '2022-10-19T01:12:20Z')

    def test_mcds_get_time(self, mcds=mcds):
        r_time = mcds.get_time()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(r_time)) == "<class 'float'>") and \
              (r_time == 1440.0)

    def test_mcds_get_runtime(self, mcds=mcds):
        r_runtime = mcds.get_runtime()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(r_runtime)) == "<class 'float'>") and \
              (r_runtime == 35.033598)


## mesh related functions ##

class TestPyMcdsMesh(object):
    ''' tests for pcdl.pyMCDS mesh related functions. '''
    mcds = pcdl.pyMCDS(xmlfile=s_file_2d, output_path=s_path_2d, custom_type={}, microenv=True, graph=True, settingxml='PhysiCell_settings.xml', verbose=True)

    def test_mcds_get_voxel_ijk_range(self, mcds=mcds):
        lti_range = mcds.get_voxel_ijk_range()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(lti_range)) == "<class 'list'>") and \
              (str(type(lti_range[0])) == "<class 'tuple'>") and \
              (str(type(lti_range[0][0])) == "<class 'int'>") and \
              (lti_range == [(0, 10), (0, 10), (0, 0)])

    def test_mcds_get_mesh_mnp_range(self, mcds=mcds):
        ltr_range = mcds.get_mesh_mnp_range()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(ltr_range)) == "<class 'list'>") and \
              (str(type(ltr_range[0])) == "<class 'tuple'>") and \
              (str(type(ltr_range[0][0])) == "<class 'numpy.float64'>") and \
              (ltr_range == [(-15, 285), (-10, 190), (0, 0)])

    def test_mcds_get_xyz_range(self, mcds=mcds):
        ltr_range = mcds.get_xyz_range()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(ltr_range)) == "<class 'list'>") and \
              (str(type(ltr_range[0])) == "<class 'tuple'>") and \
              (str(type(ltr_range[0][0])) == "<class 'numpy.float64'>") and \
              (ltr_range == [(-30, 300), (-20, 200), (-5, 5)])

    def test_mcds_get_voxel_ijk_axis(self, mcds=mcds):
        lai_axis = mcds.get_voxel_ijk_axis()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(lai_axis)) == "<class 'list'>") and \
              (str(type(lai_axis[0])) == "<class 'numpy.ndarray'>") and \
              (str(type(lai_axis[0][0])).startswith("<class 'numpy.int")) and \
              (len(lai_axis) == 3) and \
              (lai_axis[0].shape == (11,)) and \
              (lai_axis[1].shape == (11,)) and \
              (lai_axis[2].shape == (1,))

    def test_mcds_get_mesh_mnp_axis(self, mcds=mcds):
        lar_axis = mcds.get_mesh_mnp_axis()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(lar_axis)) == "<class 'list'>") and \
              (str(type(lar_axis[0])) == "<class 'numpy.ndarray'>") and \
              (str(type(lar_axis[0][0])) == "<class 'numpy.float64'>") and \
              (len(lar_axis) == 3) and \
              (lar_axis[0].shape == (11,)) and \
              (lar_axis[1].shape == (11,)) and \
              (lar_axis[2].shape == (1,))

    def test_mcds_get_mesh_flat_false(self, mcds=mcds):
        aar_mesh = mcds.get_mesh(flat=False)
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(aar_mesh)) == "<class 'numpy.ndarray'>") and \
              (aar_mesh.dtype == np.float64) and \
              (aar_mesh.shape == (3, 11, 11, 1))

    def test_mcds_get_mesh_flat_true(self, mcds=mcds):
        aar_mesh = mcds.get_mesh(flat=True)
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(aar_mesh)) == "<class 'numpy.ndarray'>") and \
              (aar_mesh.dtype == np.float64) and \
              (aar_mesh.shape == (2, 11, 11))

    def test_mcds_get_mesh_2d(self, mcds=mcds):
        aar_mesh_flat = mcds.get_mesh(flat=True)
        aar_mesh_2d = mcds.get_mesh_2D()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(aar_mesh_2d)) == "<class 'numpy.ndarray'>") and \
              (aar_mesh_2d.dtype == np.float64) and \
              (aar_mesh_2d.shape == (2, 11, 11))

    def test_mcds_get_mesh_coordinate(self, mcds=mcds):
        # cube coordinates
        ar_m_cube, ar_n_cube, ar_p_cube = mcds.get_mesh(flat=False)
        er_m_cube = set(ar_m_cube.flatten())
        er_n_cube = set(ar_n_cube.flatten())
        er_p_cube = set(ar_p_cube.flatten())
        # linear coordinates
        aar_voxel = mcds.get_mesh_coordinate()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(aar_voxel)) == "<class 'numpy.ndarray'>") and \
              (aar_voxel.dtype == np.float64) and \
              (aar_voxel.shape == (3, 121)) and \
              (set(aar_voxel[0]) == er_m_cube) and \
              (set(aar_voxel[1]) == er_n_cube) and \
              (set(aar_voxel[2]) == er_p_cube)

    def test_mcds_get_voxel_volume(self, mcds=mcds):
        r_volume = mcds.get_voxel_volume()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(r_volume)) == "<class 'numpy.float64'>") and \
              (r_volume == 6000.0)

    # bue: check else in 3D
    def test_mcds_get_mesh_spacing(self, mcds=mcds):
        lr_spacing = mcds.get_mesh_spacing()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(lr_spacing)) == "<class 'list'>") and \
              (str(type(lr_spacing[0])) == "<class 'numpy.float64'>") and \
              (str(type(lr_spacing[1])) == "<class 'numpy.float64'>") and \
              (str(type(lr_spacing[-1])) == "<class 'numpy.float64'>") and \
              (lr_spacing == [30.0, 20.0, 1.0])

    def test_mcds_get_voxel_spacing(self, mcds=mcds):
        lr_spacing = mcds.get_voxel_spacing()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(lr_spacing)) == "<class 'list'>") and \
              (str(type(lr_spacing[0])) == "<class 'numpy.float64'>") and \
              (str(type(lr_spacing[-1])) == "<class 'numpy.float64'>") and \
              (lr_spacing == [30.0, 20.0, 10.0])

    def test_mcds_is_in_mesh(self, mcds=mcds):
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (mcds.is_in_mesh(x=0, y=0, z=0, halt=False)) and \
              (not mcds.is_in_mesh(x=301, y=0, z=0, halt=False)) and \
              (not mcds.is_in_mesh(x=0, y=201, z=0, halt=False)) and \
              (not mcds.is_in_mesh(x=0, y=0, z=6, halt=False))

    def test_mcds_get_voxel_ijk(self, mcds=mcds):
        li_voxel_0 = mcds.get_voxel_ijk(x=0, y=0, z=0, is_in_mesh=True) # if b_calc
        li_voxel_1 = mcds.get_voxel_ijk(x=15, y=10, z=0, is_in_mesh=True) # if b_calc
        li_voxel_2 = mcds.get_voxel_ijk(x=30, y=20, z=0, is_in_mesh=True) # if b_calc
        li_voxel_none = mcds.get_voxel_ijk(x=-31, y=-21, z=-6, is_in_mesh=True) # else b_calc
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(li_voxel_0)) == "<class 'list'>") and \
              (str(type(li_voxel_0[0])) == "<class 'int'>") and \
              (li_voxel_0 == [0, 0, 0]) and \
              (li_voxel_1 == [1, 1, 0]) and \
              (li_voxel_2 == [2, 2, 0]) and \
              (li_voxel_none is None)


## micro environment related functions ##

class TestPyMcdsMicroenv(object):
    ''' tests for pcdl.pyMCDS micro environment related functions. '''
    mcds = pcdl.pyMCDS(xmlfile=s_file_2d, output_path=s_path_2d, custom_type={}, microenv=True, graph=True, settingxml='PhysiCell_settings.xml', verbose=True)

    def test_mcds_get_substrate_name(self, mcds=mcds):
        ls_substrate = mcds.get_substrate_names()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(ls_substrate)) == "<class 'list'>") and \
              (str(type(ls_substrate[0])) == "<class 'str'>") and \
              (ls_substrate == ['oxygen'])

    def test_mcds_get_substrate_dict(self, mcds=mcds):
        ds_substrate = mcds.get_substrate_dict()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(ds_substrate)) == "<class 'dict'>") and \
              (str(type(ds_substrate['0'])) == "<class 'str'>") and \
              (len(ds_substrate) == 1)

    def test_mcds_get_substrate_df(self, mcds=mcds):
        df_substrate = mcds.get_substrate_df()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_substrate)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (df_substrate.shape == (1, 2))

    def test_mcds_get_concentration_zslice_none(self, mcds=mcds):
        ar_conc = mcds.get_concentration(substrate='oxygen', z_slice=None)
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(ar_conc)) == "<class 'numpy.ndarray'>") and \
              (ar_conc.dtype == np.float64) and \
              (ar_conc.shape == (11, 11, 1))

    def test_mcds_get_concentration_zslice_meshcenter(self, mcds=mcds):
        ar_conc = mcds.get_concentration(substrate='oxygen', z_slice=0, halt=False)
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(ar_conc)) == "<class 'numpy.ndarray'>") and \
              (ar_conc.dtype == np.float64) and \
              (ar_conc.shape == (11, 11))

    def test_mcds_get_concentration_zslice_notmeshcenter(self, mcds=mcds):
        ar_conc = mcds.get_concentration(substrate='oxygen', z_slice=-3.333, halt=False)
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(ar_conc)) == "<class 'numpy.ndarray'>") and \
              (ar_conc.dtype == np.float64) and \
              (ar_conc.shape == (11, 11))

    def test_mcds_get_concentration_at_inmeash(self, mcds=mcds):
        ar_conc = mcds.get_concentration_at(x=0, y=0, z=0)
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(ar_conc)) == "<class 'numpy.ndarray'>") and \
              (ar_conc.dtype == np.float64) and \
              (ar_conc.shape == (1,))

    def test_mcds_get_concentration_at_notinmeash(self, mcds=mcds):
        ar_conc = mcds.get_concentration_at(x=-31, y=-21, z=-6)
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (ar_conc is None)

    def test_mcds_get_concentration_df(self, mcds=mcds):
        df_conc = mcds.get_concentration_df(z_slice=None, halt=False, values=1, drop=set(), keep=set())
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_conc)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (df_conc.shape == (121, 10))

    def test_mcds_get_conc_df(self, mcds=mcds):
        df_conc = mcds.get_conc_df(z_slice=None, halt=False, values=1, drop=set(), keep=set())
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_conc)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (df_conc.shape == (121, 10))

    def test_mcds_get_conc_df_zslice_center(self, mcds=mcds):
        df_conc = mcds.get_conc_df(z_slice=0, halt=False, values=1, drop=set(), keep=set())
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_conc)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (df_conc.shape == (121, 10))

    def test_mcds_get_conc_df_zslice_outofcenter(self, mcds=mcds):
        df_conc = mcds.get_conc_df(z_slice=-6, halt=False, values=1, drop=set(), keep=set())
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_conc)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (df_conc.shape == (121, 10))

    def test_mcds_get_conc_df_values(self, mcds=mcds):
        df_conc = mcds.get_conc_df(z_slice=None, halt=False, values=2, drop=set(), keep=set())
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_conc)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (df_conc.shape == (121, 10))

    def test_mcds_get_conc_df_drop(self, mcds=mcds):
        df_conc = mcds.get_conc_df(z_slice=None, halt=False, values=1, drop={'oxygen'}, keep=set())
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_conc)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (df_conc.shape == (121, 9))

    def test_mcds_get_conc_df_keep(self, mcds=mcds):
        df_conc = mcds.get_conc_df(z_slice=None, halt=False, values=1, drop=set(), keep={'oxygen'})
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_conc)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (df_conc.shape == (121, 10))

    def test_mcds_plot_contour(self, mcds=mcds):
        fig = mcds.plot_contour(
            'oxygen',
            z_slice = -3.333,  # test if
            vmin = None,  # test if
            vmax = None,  # test if
            #alpha = 1,  # matplotlib
            fill = False,  # contour case
            #cmap = 'viridis',  matplotlib
            title = 'test_mcds_plot_contour',  # test if
            #grid = False, # matplotlib
            xlim = [-31, 301],  # test if
            ylim = [-21, 201],  # test if
            xyequal = True, # test if
            figsize = None,  # test if
            ax = None  # generate fig ax case
        )
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(fig)) == "<class 'matplotlib.figure.Figure'>")

    def test_mcds_plot_contourf(self, mcds=mcds):
        fig = mcds.plot_contour(
            'oxygen',
            z_slice = 0,  # jum over if
            vmin = None,  # test if
            vmax = None,  # test if
            #alpha = 1,  # matplotlib
            fill = True,  # contourf case
            #cmap = 'viridis',  # matplotlib
            title = 'test_mcds_plot_contourf',  # test if
            #grid = True,  # matplotlib
            xlim = None,  # jump over if
            ylim = None,  # jump over if
            xyequal = True,  # test if
            figsize = None,  # test if
            ax = None  # generate fig ax case
        )
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(fig)) == "<class 'matplotlib.figure.Figure'>")


## cell related functions ##

class TestPyMcdsCell(object):
    ''' tests for pcdl.pyMCDS cell related functions. '''
    mcds = pcdl.pyMCDS(xmlfile=s_file_2d, output_path=s_path_2d, custom_type={}, microenv=True, graph=True, settingxml='PhysiCell_settings.xml', verbose=True)

    def test_mcds_get_cell_variables(self, mcds=mcds):
        ls_variable = mcds.get_cell_variables()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(ls_variable)) == "<class 'list'>") and \
              (str(type(ls_variable[0])) == "<class 'str'>") and \
              (len(ls_variable) == 77)

    def test_mcds_get_celltype_dict(self, mcds=mcds):
        ds_celltype = mcds.get_celltype_dict()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(ds_celltype)) == "<class 'dict'>") and \
              (str(type(ds_celltype['0'])) == "<class 'str'>") and \
              (len(ds_celltype) == 1)

    def test_mcds_get_cell_df(self, mcds=mcds):
        df_cell = mcds.get_cell_df(values=1, drop=set(), keep=set())
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_cell)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (df_cell.shape == (1099, 95))

    def test_mcds_get_cell_df_values(self, mcds=mcds):
        df_cell = mcds.get_cell_df(values=2, drop=set(), keep=set())
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_cell)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (df_cell.shape == (1099, 40))

    def test_mcds_get_cell_df_drop(self, mcds=mcds):
        df_cell = mcds.get_cell_df(values=1, drop={'oxygen'}, keep=set())
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_cell)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (df_cell.shape == (1099, 94))

    def test_mcds_get_cell_df_keep(self, mcds=mcds):
        df_cell = mcds.get_cell_df(values=1, drop=set(), keep={'oxygen'})
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_cell)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (df_cell.shape == (1099, 13))

    def test_mcds_get_cell_df_at_inmeash(self, mcds=mcds):
        df_cell = mcds.get_cell_df_at(x=0, y=0, z=0, values=1, drop=set(), keep=set())
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(df_cell)) == "<class 'pandas.core.frame.DataFrame'>") and \
              (df_cell.shape == (5, 95))

    def test_mcds_get_cell_df_at_notinmeash(self, mcds=mcds):
        df_cell = mcds.get_cell_df_at(x=-31, y=-21, z=-6, values=1, drop=set(), keep=set())
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (df_cell is None)

    # scatter categorical
    def test_mcds_plot_scatter_cat_if(self, mcds=mcds):
        fig = mcds.plot_scatter(
            focus='cell_type',  # case categorical
            z_slice = -3.333,   # test if
            z_axis = None,  # test if case categorical
            #alpha = 1,  # matplotlib
            cmap = 'viridis',  # else case es_categorical
            title = 'test_mcds_plot_scatter_cat', # matplotlib
            #grid = True,  # matplotlib
            #legend_loc = 'lower left',  # matplotlib
            xlim = None,  # test if
            ylim = None,  # test if
            xyequal = True,  # test if
            #s = None,  # matplotlib
            figsize = None,  # test if case ax none
            ax = None,  # generate matplotlib figure
        )
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(fig)) == "<class 'matplotlib.figure.Figure'>")

    def test_mcds_plot_scatter_cat_else1(self, mcds=mcds):
        fig = mcds.plot_scatter(
            focus='cell_type',  # case categorical
            z_slice = 0,  # jump over if
            z_axis = {'cancer_cell'},  # test else case categorical
            #alpha = 1,  # matplotlib
            cmap = {'cancer_cell': 'maroon'},  # test if case es_categorical
            title ='test_mcds_plot_scatter_else',  # matplotlib
            #grid = True,  # matplotlib
            #legend_loc = 'lower left',  # matplotlib
            xlim = [-31, 301],  # jump over if
            ylim = [-21, 201],  # jump over if
            xyequal = False,  # jump over if
            #s = None,  # matplotlib
            figsize = [7.0, 5.0],  # jump over if case ax none
            ax = None,  # use axis from existing matplotlib figure
        )
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(fig)) == "<class 'matplotlib.figure.Figure'>")

    def test_mcds_plot_scatter_cat_else2(self, mcds=mcds):
        fig, ax = plt.subplots()
        mcds.plot_scatter(
            focus='cell_type',  # case categorical
            z_slice = 0,  # jump over if
            z_axis = {'cancer_cell'},  # test else case categorical
            #alpha = 1,  # matplotlib
            cmap = 'viridis',  # test else case es_categorical
            title ='test_mcds_plot_scatter_else2',  # matplotlib
            #grid = True,  # matplotlib
            #legend_loc = 'lower left',  # matplotlib
            xlim = None,  # test if
            ylim = None,  # test if
            xyequal = True,  # test if
            #s = None,  # matplotlib
            #figsize = None,  # test case ax ax
            ax = ax,  # use axis from existing matplotlib figure
        )
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(fig)) == "<class 'matplotlib.figure.Figure'>")

    # scatter numerical
    def test_mcds_plot_scatter_num_if(self, mcds=mcds):
        fig = mcds.plot_scatter(
            focus='oxygen',  # case numeric
            z_slice = -3.333,   # test if
            z_axis = None,  # test if numeric
            #alpha = 1,  # matplotlib
            #cmap = 'viridis',  # matplotlib
            #title = None, # matplotlib
            #grid = True,  # matplotlib
            #legend_loc = 'lower left',  # matplotlib
            xlim = None,  # test if
            ylim = None,  # test if
            #xyequal = True,  # test if
            #s = None,  # matplotlib
            #figsize = None,  # test if case
            #ax = None,  # generate matplotlib figure
        )
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(fig)) == "<class 'matplotlib.figure.Figure'>")

    def test_mcds_plot_scatter_num_else(self, mcds=mcds):
        fig = mcds.plot_scatter(
            focus='oxygen',  # case numeric
            z_slice = 0,   # jump over if
            z_axis = [0, 38],  # test else numeric
            #alpha = 1,  # matplotlib
            #cmap = 'viridis',  # matplotlib
            #title = None, # matplotlib
            #grid = True,  # matplotlib
            #legend_loc = 'lower left',  # matplotlib
            xlim = None,  # test if
            ylim = None,  # test if
            #xyequal = True,  # test if
            #s = None,  # matplotlib
            #figsize = None,  # if case
            #ax = None,  # generate matplotlib figure
        )
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(fig)) == "<class 'matplotlib.figure.Figure'>")


## graph related functions ##

class TestPyMcdsGraph(object):
    ''' tests for pcdl.pyMCDS graph related functions. '''
    mcds = pcdl.pyMCDS(xmlfile=s_file_2d, output_path=s_path_2d, custom_type={}, microenv=True, graph=True, settingxml='PhysiCell_settings.xml', verbose=True)

    # graph dictionatry
    def test_mcds_get_attached_graph_dict(self, mcds=mcds):
        dei_graph = mcds.data['discrete_cells']['graph']['attached_cells']
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(dei_graph)) == "<class 'dict'>") and \
              (str(type(dei_graph[0])) == "<class 'set'>") and \
              (len(dei_graph[0]) == 0) and \
              (len(dei_graph) == 1099)

    def test_mcds_get_nighbor_graph_dict(self, mcds=mcds):
        dei_graph = mcds.data['discrete_cells']['graph']['neighbor_cells']
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(dei_graph)) == "<class 'dict'>") and \
              (str(type(dei_graph[0])) == "<class 'set'>") and \
              (len(dei_graph[0]) == 7) and \
              (str(type(next(iter(dei_graph)))) == "<class 'int'>") and \
              (len(dei_graph) == 1099)

    # attached graph gml files
    def test_mcds_make_graph_gml_attached_defaultattr(self, mcds=mcds):
        s_pathfile = mcds.make_graph_gml(graph_type='attached', edge_attr=True, node_attr=[])
        f = open(s_pathfile)
        s_file = f.read()
        f.close()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (s_pathfile.replace('\\','/').endswith('pcdl/data_timeseries_2d/output00000024_attached.gml')) and \
              (os.path.exists(s_pathfile)) and \
              (s_file.find('Creator "pcdl_v') > -1) and \
              (s_file.find('graph [\n  id 1440\n  comment "time_min"\n  label "attached_graph"\n  directed 0\n') > -1) and \
              (s_file.find('node [\n    id') > -1) and \
              (s_file.find('edge [\n    source') == -1) and \
              (s_file.find('distance_microns') == -1)
        os.remove(s_pathfile)

    def test_mcds_make_graph_gml_attached_edgeattrfalse(self, mcds=mcds):
        s_pathfile = mcds.make_graph_gml(graph_type='attached', edge_attr=False, node_attr=[])
        f = open(s_pathfile)
        s_file = f.read()
        f.close()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (s_pathfile.replace('\\','/').endswith('pcdl/data_timeseries_2d/output00000024_attached.gml')) and \
              (os.path.exists(s_pathfile)) and \
              (s_file.find('Creator "pcdl_v') > -1) and \
              (s_file.find('graph [\n  id 1440\n  comment "time_min"\n  label "attached_graph"\n  directed 0\n') > -1) and \
              (s_file.find('node [\n    id') > -1) and \
              (s_file.find('edge [\n    source') == -1) and \
              (s_file.find('distance_microns') == -1)
        os.remove(s_pathfile)

    def test_mcds_make_graph_gml_neighbor_nodeattrtrue(self, mcds=mcds):
        s_pathfile = mcds.make_graph_gml(graph_type='neighbor', edge_attr=True, node_attr=['dead','cell_count_voxel','cell_density_micron3','cell_type'])  # bool,int,float,str
        f = open(s_pathfile)
        s_file = f.read()
        f.close()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (s_pathfile.replace('\\','/').endswith('pcdl/data_timeseries_2d/output00000024_neighbor.gml')) and \
              (os.path.exists(s_pathfile)) and \
              (s_file.find('Creator "pcdl_v') > -1) and \
              (s_file.find('graph [\n  id 1440\n  comment "time_min"\n  label "neighbor_graph"\n  directed 0\n') > -1) and \
              (s_file.find('node [\n    id') > -1) and \
              (s_file.find('dead') == -1) and \
              (s_file.find('cell_count_voxel') == -1) and \
              (s_file.find('cell_density_micron3') == -1) and \
              (s_file.find('cell_type') == -1) and \
              (s_file.find('edge [\n    source') > -1) and \
              (s_file.find('distance_microns')> -1)
        os.remove(s_pathfile)

    # neighbor graph gml file
    def test_mcds_make_graph_gml_neighbor_defaultattr(self, mcds=mcds):
        s_pathfile = mcds.make_graph_gml(graph_type='neighbor', edge_attr=True, node_attr=[])
        f = open(s_pathfile)
        s_file = f.read()
        f.close()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (s_pathfile.replace('\\','/').endswith('pcdl/data_timeseries_2d/output00000024_neighbor.gml')) and \
              (os.path.exists(s_pathfile)) and \
              (s_file.find('Creator "pcdl_v') > -1) and \
              (s_file.find('graph [\n  id 1440\n  comment "time_min"\n  label "neighbor_graph"\n  directed 0\n') > -1) and \
              (s_file.find('node [\n    id') > -1) and \
              (s_file.find('edge [\n    source') > -1) and \
              (s_file.find('distance_microns') > -1)
        os.remove(s_pathfile)

    def test_mcds_make_graph_gml_neighbor_edgeattrfalse(self, mcds=mcds):
        s_pathfile = mcds.make_graph_gml(graph_type='neighbor', edge_attr=False, node_attr=[])
        f = open(s_pathfile)
        s_file = f.read()
        f.close()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (s_pathfile.replace('\\','/').endswith('pcdl/data_timeseries_2d/output00000024_neighbor.gml')) and \
              (os.path.exists(s_pathfile)) and \
              (s_file.find('Creator "pcdl_v') > -1) and \
              (s_file.find('graph [\n  id 1440\n  comment "time_min"\n  label "neighbor_graph"\n  directed 0\n') > -1) and \
              (s_file.find('node [\n    id') > -1) and \
              (s_file.find('edge [\n    source') > -1) and \
              (s_file.find('distance_microns') == -1)
        os.remove(s_pathfile)

    def test_mcds_make_graph_gml_neighbor_nodeattrtrue(self, mcds=mcds):
        s_pathfile = mcds.make_graph_gml(graph_type='neighbor', edge_attr=True, node_attr=['dead','cell_count_voxel','cell_density_micron3','cell_type'])  # bool,int,float,str
        f = open(s_pathfile)
        s_file = f.read()
        f.close()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (s_pathfile.replace('\\','/').endswith('pcdl/data_timeseries_2d/output00000024_neighbor.gml')) and \
              (os.path.exists(s_pathfile)) and \
              (s_file.find('Creator "pcdl_v') > -1) and \
              (s_file.find('graph [\n  id 1440\n  comment "time_min"\n  label "neighbor_graph"\n  directed 0\n') > -1) and \
              (s_file.find('node [\n    id') > -1) and \
              (s_file.find('dead') > -1) and \
              (s_file.find('cell_count_voxel') > -1) and \
              (s_file.find('cell_density_micron3') > -1) and \
              (s_file.find('cell_type') > -1) and \
              (s_file.find('edge [\n    source') > -1) and \
              (s_file.find('distance_microns') > -1)
        os.remove(s_pathfile)


## model setting related functions ##

class TestPyMcdsSetting(object):
    ''' tests for pcdl.pyMCDS setting related functions. '''
    mcds = pcdl.pyMCDS(xmlfile=s_file_2d, output_path=s_path_2d, custom_type={}, microenv=True, graph=True, settingxml='PhysiCell_settings.xml', verbose=True)

    def test_mcds_get_parameter_dict(self, mcds=mcds):
        d_parameter = mcds.get_parameter_dict()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(d_parameter)) == "<class 'dict'>") and \
              (len(d_parameter) == 63) and \
              (d_parameter['oxygen_initial_condition'] == 38.0)

    def test_mcds_get_rule_df(self, mcds=mcds):
        df_rule = mcds.get_rule_df()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (df_rule is None)

    def test_mcds_get_unit_dict(self, mcds=mcds):
        ds_unit = mcds.get_unit_dict()
        assert(str(type(mcds)) == "<class 'pcdl.pyMCDS.pyMCDS'>") and \
              (str(type(ds_unit)) == "<class 'dict'>") and \
              (len(ds_unit) == 121) and \
              (ds_unit['oxygen'] == 'mmHg')

