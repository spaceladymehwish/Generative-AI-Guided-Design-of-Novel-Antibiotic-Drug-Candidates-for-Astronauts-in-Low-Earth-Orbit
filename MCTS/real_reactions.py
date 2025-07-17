from rdkit import Chem

REAL_REACTIONS = [
    {
        "reactants": [
            Chem.MolFromSmarts('CC(C)(C)OC(=O)[N:1]([*:2])[*:3].[*:4][N:5]([H])[*:6]'),
            Chem.MolFromSmarts('[OH1][C:7]([*:8])=[O:9]'),
            Chem.MolFromSmarts('[OH1][C:10]([*:11])=[O:12]')
        ],
        "product": Chem.MolFromSmarts('[*:4][N:5]([*:6])[C:7](=[O:9])[*:8].[*:3][N:1]([*:2])[C:10](=[O:12])[*:11]'),
        "reaction_id": 275592
    },
    {
        "reactants": [
            Chem.MolFromSmarts('[*:1][N:2]([H])[*:3]'),
            Chem.MolFromSmarts('[OH1][C:4]([*:5])=[O:6]')
        ],
        "product": Chem.MolFromSmarts('[*:5][C:4](=[O:6])[N:2]([*:1])[*:3]'),
        "reaction_id": 22
    },
    {
        "reactants": [
            Chem.MolFromSmarts('[*:1][N:2]([H])[*:3]'),
            Chem.MolFromSmarts('[OH1][C:4]([*:5])=[O:6]')
        ],
        "product": Chem.MolFromSmarts('[*:5][C:4](=[O:6])[N:2]([*:1])[*:3]'),
        "reaction_id": 11
    },
    {
        "reactants": [
            Chem.MolFromSmarts('[*:1][N:2]([H])[*:3]'),
            Chem.MolFromSmarts('[OH1][C:4]([*:5])=[O:6]')
        ],
        "product": Chem.MolFromSmarts('[*:5][C:4](=[O:6])[N:2]([*:1])[*:3]'),
        "reaction_id": 527
    },
    {
        "reactants": [
            Chem.MolFromSmarts('[*:1][N:2]([H])[*:3]'),
            Chem.MolFromSmarts('[OH1][C:4]([*:5])=[O:6]')
        ],
        "product": Chem.MolFromSmarts('[*:5][C:4](=[O:6])[N:2]([*:1])[*:3]'),
        "reaction_id": 240690
    },
    {
        "reactants": [
            Chem.MolFromSmarts('[*:1][N:2]([H])[H:3]'),
            Chem.MolFromSmarts('[*:4][N:5]([H])[*:6]')
        ],
        "product": Chem.MolFromSmarts('O=C([N:2]([*:1])[H:3])[N:5]([*:4])[*:6]'),
        "reaction_id": 2430
    },
    {
        "reactants": [
            Chem.MolFromSmarts('[*:1][N:2]([H])[H:3]'),
            Chem.MolFromSmarts('[*:4][N:5]([H])[H:6]')
        ],
        "product": Chem.MolFromSmarts('O=C([N:2]([*:1])[H:3])[N:5]([*:4])[H:6]'),
        "reaction_id": 2708
    },
    {
        "reactants": [
            Chem.MolFromSmarts('[*:1][N:2]([H])[*:3]'),
            Chem.MolFromSmarts('[F,Cl,Br,I][*:4]')
        ],
        "product": Chem.MolFromSmarts('[*:1][N:2]([*:3])[*:4]'),
        "reaction_id": 2230
    },
    {
        "reactants": [
            Chem.MolFromSmarts('[*:1][N:2]([H])[H:3]'),
            Chem.MolFromSmarts('[*:4][N:5]([H])[H:6]')
        ],
        "product": Chem.MolFromSmarts('O=C(C(=O)[N:2]([*:1])[H:3])[N:5]([*:4])[H:6]'),
        "reaction_id": 2718
    },
    {
        "reactants": [
            Chem.MolFromSmarts('[*:1][N:2]([H])[*:3]'),
            Chem.MolFromSmarts('[O:4]=[S:5](=[O:6])([F,Cl,Br,I])[*:7]')
        ],
        "product": Chem.MolFromSmarts('[O:4]=[S:5](=[O:6])([*:7])[N:2]([*:1])[*:3]'),
        "reaction_id": 40
    },
    {
        "reactants": [
            Chem.MolFromSmarts('[*:1][N:2]([H])[*:3]'),
            Chem.MolFromSmarts('[F,Cl,Br,I][*:4]')
        ],
        "product": Chem.MolFromSmarts('[*:1][N:2]([*:3])[*:4]'),
        "reaction_id": 27
    },
    {
        "reactants": [
            Chem.MolFromSmarts('[*:1][N:2]([H])[*:3]'),
            Chem.MolFromSmarts('[*:4][N:5]([H])[H:6]')
        ],
        "product": Chem.MolFromSmarts('O=C(C(=O)[N:2]([*:1])[*:3])[N:5]([*:4])[H:6]'),
        "reaction_id": 271948
    },
    {
        "reactants": [
            Chem.MolFromSmarts('[OH1:1][C:2]([*:3])=[O:4]'),
            Chem.MolFromSmarts('[F,Cl,Br,I][*:5]')
        ],
        "product": Chem.MolFromSmarts('[O:4]=[C:2]([*:3])[O:1][*:5]'),
        "reaction_id": 1458
    }
]
