import pandas as pd

import dock
import protein
import tools



def main():
    path = '../data/clean/1jme_clean.pdb'
    wt = '''MTIKEMPQPKTFGELKNLPLLNTDKPVQALMKIADELGEIFKFEAPGRVTRYLSSQRLIKE\
    ACDESRFDKNLSQALKFVRDFAGDGLFTSWTHEKNWKKAHNILLPSFSQQAMKGYHAMMVDIAVQLVQK\
    WERLNADEHIEVPEDMTRLTLDTIGLCGFNYRFNSFYRDQPHPFITSMVRALDEAMNKLQRANPDDPAY\
    DENKRQFQEDIKVMNDLVDKIIADRKASGEQSDDLLTHMLNGKDPETGEPLDDENIRYQIITFLIAGHE\
    TTSGLLSFALYFLVKNPHVLQKAAEEAARVLVDPVPSYKQVKQLKYVGMVLNEALRLWPTAPAFSLYAK\
    EDTVLGGEYPLEKGDELMVLIPQLHRDKTIWGDDVEEFRPERFENPSAIPQHAFKPFGNGQRACIGQQF\
    ALHEATLVLGMMLKHFDFEDHTNYELDIKETLTLKPEGFVVKAKSKKIPLGGIPSPSTEQSAKKVRKKAEN'''.replace(' ','')


    bm3 = protein.protein(pdb_path = '../data/clean/1jme_clean.pdb', seq = wt)
    for i in range(80,90):
        bm3.mutate(i, 'A')
    bm3.fold()

    df = pd.read_csv('../data/cpds/HRAC_Herbicides.csv')
    vina = dock.Vina(bm3)


if __name__ == '__main__':
    main()