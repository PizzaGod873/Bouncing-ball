�
    -9,g0  �                   ��  � S SK r S SKrS SKrS SKr " S S5      rS rS r\ R                  " 5         Sr	Sr
SrS	rS	r\ R                  R                  \\45      r\ R"                  R%                  5       r\R(                  " \S
-  \S
-  /\R*                  S9rSrSr\R(                  " \S
-  \S
-  S-
  /\R*                  S9r\R(                  " S S /\R*                  S9r\" \\5      /rSrSrSr\R>                  " \* S
-  5      r \R>                  " \S
-  5      r!Sr"\"(       GaI  \ RF                  RI                  5        H!  r#\#RJ                  \ RL                  :X  d  M  Sr"M#     \ \-  r \!\-  r!\ GHM  r'\'RP                  S   \:�  d9  \'RP                  S    S :  d&  \'RP                  S    \:�  d  \'RP                  S   S :  a�  \RS                  \'5        \RU                  \" \S
-  \S
-  S-
  /\RV                  " SS5      \RV                  " SS5      /S95        \RU                  \" \S
-  \S
-  S-
  /\RV                  " SS5      \RV                  " SS5      /S95        \'RX                  S==   \-  ss'   \'=RP                  \'RX                  -  sl(        \RZ                  R]                  \'RP                  \-
  5      r/\/\-   \:�  d  GMU  \" \'RP                  \\ \!5      (       a  S\'l0        \'R`                  S:X  d  GM�  \'RP                  \-
  r1\1\RZ                  R]                  \15      -  r2\\\-
  \2-  -   \'l(        \R(                  " \1S   * \1S    /\R*                  S9r3\Rh                  " \'RX                  \35      \Rh                  " \3\35      -  \3-  r5S
\5-  \'RX                  -
  \'l,        \'=RX                  \3\-  -  sl,        GMP     \Rm                  \	5        \ Rn                  Rq                  \\
\\S5        \" \\\\ \!5        \ H5  r'\ Rn                  Rq                  \\'Rr                  \'RP                  \5        M7     \ R                  Ru                  5         \Rw                  S5        \"(       a  GMI  \ Rx                  " 5         g)�    Nc                   �   � \ rS rSrS rSrg)�Ball�   c                 �D  � [         R                  " U[         R                  S9U l        [         R                  " U[         R                  S9U l        [
        R                  " SS5      [
        R                  " SS5      [
        R                  " SS5      4U l        SU l        g )N��dtyper   ��   T)	�np�array�float64�pos�v�random�randint�color�is_in)�self�position�velocitys      �a.py�__init__�Ball.__init__   sf   � ��8�8�H�B�J�J�7������(�"�*�*�5����n�n�Q��,�f�n�n�Q��.D�f�n�n�UV�X[�F\�]��
���
�    )r   r   r   r   N)�__name__�
__module__�__qualname__�__firstlineno__r   �__static_attributes__� r   r   r   r      s   � �r   r   c                 �t  � XS-   [         R                  " [        R                  " U5      [        R                  " U5      /5      -  -   nXS-   [         R                  " [        R                  " U5      [        R                  " U5      /5      -  -   n[
        R                  R                  U [        XU/S5        g )Ni�  r   )	r
   r   �math�cos�sin�pygame�draw�polygon�BLACK)�window�center�radius�start_angle�	end_angle�p1�p2s          r   �draw_arcr/      s�   � �	�D�=�B�H�H�d�h�h�{�.C�T�X�X�k�EZ�-[�$\�\�	\�B�	�D�=�B�H�H�d�h�h�y�.A�4�8�8�I�CV�-W�$X�X�	X�B�
�K�K������B�'7��;r   c                 �P  � U S   US   -
  nU S   US   -
  n[         R                  " XT5      nUS[         R                  -  -  nUS[         R                  -  -  nX#:�  a  US[         R                  -  -  nX&s=::  a  U::  d&  O  X&S[         R                  -  -   s=::  a  U::  a   g  g gg )Nr   �   �   T)r!   �atan2�pi)�ball_pos�CIRCLE_CENTERr+   r,   �dx�dy�
ball_angles          r   �is_ball_in_arcr:      s�   � �	�!��}�Q�'�	'�B�	�!��}�Q�'�	'�B����B�#�J��Q����[�)�I���T�W�W��-�K����Q����[� �	��-�I�-�+�a�RV�RY�RY�k�AY�2f�]f�2f�� 3g�� 3gr   )r   r   r   )r	   �   r   )r	   r   r   i   r2   r   �   �   �x   g�������?g{�G�z�?�<   TFr1   ������   �����)r   r   �   )=r$   �numpyr
   r!   r   r   r/   r:   �initr'   �ORANGE�RED�WIDTH�HEIGHT�display�set_moder(   �time�Clock�clockr   r   r6   �CIRCLE_RADIUS�BALL_RADIUSr5   �ball_velocity�balls�GRAVITY�spinning_speed�
arc_degree�radiansr+   r,   �running�event�get�type�QUIT�ballr   �remove�append�uniformr   �linalg�norm�distr   �d�d_unit�t�dot�proj_v_t�fillr%   �circler   �flip�tick�quitr   r   r   �<module>rm      s(  �� � � � �� �<��$ ������	������	��	���	 �	 �%���	1������������%��'�6�!�8�,�2�:�:�>�������8�8�U�1�W�f�Q�h��n�-�R�Z�Z�@�����!�Q��r�z�z�2��	�h��	&�'��
�����
��l�l�J�;�q�=�)���L�L��A��&�	�
�� ����!�!�#���:�:����$��G� $�
 �>�!�K����I����8�8�A�;���4�8�8�A�;��?�d�h�h�q�k�E�6I�T�X�X�VW�[�[\�_��L�L����L�L��%�!�)�V�a�Z�#�5E�)F�TZ�Tb�Tb�ce�gh�Ti�kq�ky�ky�z|�~�  lA�  TB�  C�  D��L�L��%�!�)�V�a�Z�#�5E�)F�TZ�Tb�Tb�ce�gh�Ti�kq�ky�ky�z|�~�  lA�  TB�  C�  D� 	���q�	�W��	����D�F�F��� �y�y�~�~�d�h�h��6�7���+���-��d�h�h��{�I�N�N�"��
��z�z�T�!��H�H�}�,���2�9�9�>�>�!�,�,��(�M�K�,G�6�+Q�Q����H�H�q��t�e�Q�q�T�]�"�*�*�=���F�F�4�6�6�1�-�b�f�f�Q��l�:�A�=���X�����.������!�n�,�,���; �D �K�K���
�K�K���v�v�}�m�Q�G��V�]�M�;�	�J��������6�4�:�:�t�x�x��E� � �N�N����	�J�J�r�N�g �g�j ���r   