from config import Config


def config() -> Config:
    return Config(version='1.0',
                  algorithm_author=[
                      'Chris Schnaufer', 'Clairessa Brown', 'David Lebauer'
                  ],
                  algorithm_author_email=[
                      'schnaufer@arizona.edu',
                      'clairessabrown@email.arizona.edu',
                      'dlebauer@email.arizona.edu'
                  ],
                  algorithm_contributors=["Jacob van der Leeuw"],
                  algorithm_name='Greenness Transformer',
                  algorithm_description=(
                      'This algorithm performs a variety of '
                      'calculations using RGB pixels from images in order '
                      'to assess plant and crop health and growth'),
                  citation_author='Clairessa Brown',
                  citation_title='Woebbecke, D.M. et al',
                  citation_year='2020',
                  variable_names=[
                      'excess greenness index', 'green leaf index', 'cive',
                      'normalized difference index', 'excess red', 'exgr',
                      'combined indices 1', 'combined indices 2',
                      'vegetative index', 'normalized green-red difference',
                      'percent green'
                  ],
                  variable_units=[
                      '[-510:510]', '[-1:1]', '[-255:255]', '[-127:129]',
                      '[-255:255]', '[-255:332]', '[-1000:1000]',
                      '[-1000:1000]', '[-255:255]', '[-255:255]', '[0:100]'
                  ],
                  variable_labels=[
                      'excess_greenness_index', 'green_leaf_index', 'cive',
                      'normalized_difference_index(pxarray)', 'excess_red',
                      'exgr', 'combined_indices_1', 'combined_indices_2',
                      'vegetative_index', 'ngrdi', 'percent_green'
                  ],
                  write_betydb_csv=True,
                  write_geostreams_csv=True)
