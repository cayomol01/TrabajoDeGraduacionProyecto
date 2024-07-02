=====================================================================================================

ASVspoof 2019 & 2021 Challenge Databases - Mapping to VCTK and other source databases

Copyright (c) 2022  

National Institute of Informatics, Japan
EURECOM, France
University of Eastern Finland, Finland
Institute for Infocomm Research, Singapore

=====================================================================================================

1. About
 ASVspoof 2019 and 2021 databases were created on the basis of VCTK (https://doi.org/10.7488/ds/2645)
 corpus and those for Voice Conversion Challenges (VCC, http://www.vc-challenge.org/).

 Files included in this package show the mapping between utterances in the ASVspoof databases and the
 source databases. Note that for LA and DFP
  1) only bona fide utterances have corresponding utterances in the source databases.
  2) TTS-based spoofed utterances are synthesized from input text, 
  3) VC-based spoofed utterances are synthesized from source audio.

 Other metadata such as spoofing attack type or reply configuration for ASVspoof2021 can be found 
 in the official evaluation keys and metadata (https://www.asvspoof.org/index2021.html), or the protocol
 files in ASVspoof2019 packages (https://doi.org/10.7488/ds/2555).

 If you use the information included in this package for your research, please describe it explicitly
 in your paper. Please also cite the related papers listed in 5. Reference.

2. Files:
 ASVspoof2019_LA_VCTK_MetaInfo.tsv: mapping file for ASVspoof2019 LA database
 ASVspoof2019_PA_VCTK_MetaInfo.tsv: mapping file for ASVspoof2019 PA database
 ASVspoof2021_LA_VCTK_MetaInfo.tsv: mapping file for ASVspoof2021 LA database
 ASVspoof2021_PA_VCTK_MetaInfo.tsv: mapping file for ASVspoof2021 PA database
 ASVspoof2021_DF_VCTK_MetaInfo.tsv: mapping file for ASVspoof2021 DF data sourced from VCTK 
 ASVspoof2021_DF_VCC_MetaInfo.tsv:  mapping file for ASVspoof2021 DF data sourced from VCC
 
 
3. Format and Usage
 The files are in tab-separated values (tsv) format, which uses \t as the column separator. 
 You may use Panads (https://pandas.pydata.org/) to load them. 
 For example:
 >>> import pandas as pd
 >>> map_file = pd.read_csv(FILE_PATH, sep='\t', index_col = 0)

 For LA, it has five columns:
   ASVspoof_ID VCTK_ID TTS_VC_target_speaker TTS_text VC_source_VCTK_ID

   ASVspoof_ID:            ID of the trial in ASVspoof database
   VCTK_ID:                ID of the trial in VCTK database if the trial is bona fide, else '-'
   TTS_VC_target_speaker:  ID of the target speaker in VCTK database if the trial is spoofed, else '-'
   TTS_text:               input text if the spoofed trial is by text-to-speech, else '-'
   VC_source_VCTK_ID:      ID of the source audio in VCTK if the spoofed trial is by voice conversion, else '-'

   For example:
   LA_E_7911805 	- 	p299 	Now there's an even bigger target. 	-
   This is a TTS spoofed trial that mimics speaker p299 in VCTK, using text input "Now there's an ..."
   
   LA_E_6316844 	- 	p230 	- 	p277_358
   This is a VC spoofed trial that converts source audio p277_358 into a spoofed audio targeting at p230

   LA_E_9999177 	p308_342 	- 	- 	-
   This is a bona fide trial, corresponding to p308_342 in VCTK

 For PA, it has two columns:
   ASVspoof_ID VCTK_ID
   ASVspoof_ID:            ID of the trial in ASVspoof PA database
   VCTK_ID:                 ID of the trial in VCTK
 
 For DF ASVspoof2021_DF_VCTK_MetaInfo.txt has the same format as that for LA.
 For DF ASVspoof2021_DF_VCC_MetaInfo.txt, it has five columns:
   ASVspoof_ID VCC_ID TTS_VC_target_speaker TTS_text VC_source_VCC_ID

   ASVspoof_ID:            ID of the trial in ASVspoof DF database
   VCC_ID:                 ID of the trial in VCC challenge if the trial is bona fide, else '-'
   TTS_VC_target_speaker:  ID of the target speaker in VCC challenge if the trial is spoofed, else '-'
   TTS_text:               '-'
   VC_source_VCC_ID:       ID of the input audio in VCC challenge if the spoofed trial is VC-based, else '-'


4. Copying
______________________

This dataset is licensed under the Open Data Commons Attribution License (ODC-By). 

Regarding the Open Data Commons Attribution License (ODC-By), please see LICENSE.txt or 
https://opendatacommons.org/licenses/by/1.0/index.html
 
THIS DATABASE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, 
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, 
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, 
OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS DATABASE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE



5. Reference
----------------------
@article{asvspoof2019_database,
author = {Wang, Xin and Yamagishi, Junichi and Todisco, Massimiliano and Others},
doi = {10.1016/j.csl.2020.101114},
issn = {08852308},
journal = {Computer Speech \& Language},
keywords = {ASVspoof challenge,Anti-spoofing,Automatic speaker verification,Biometrics,Countermeasure,Media forensics,Presentation attack,Presentation attack detection,Replay,Text-to-speech synthesis,Voice conversion},
month = {nov},
pages = {101114},
title = {{ASVspoof 2019: A large-scale public database of synthesized, converted and replayed speech}},
volume = {64},
year = {2020}
}

@article{LiuASVspoof2021,
author = {Liu, Xuechen and Wang, Xin and Sahidullah, Md and Patino, Jose and Delgado, H{\'{e}}ctor and Kinnunen, Tomi and Todisco, Massimiliano and Yamagishi, Junichi and Evans, Nicholas and Nautsch, Andreas and Lee, Kong Aik},
journal = {arXiv preprint arXiv:2210.02437},
title = {{ASVspoof 2021: Towards Spoofed and Deepfake Speech Detection in the Wild}},
year = {2022}
}


@inproceedings{yamagishi21_asvspoof,
author = {Yamagishi, Junichi and Wang, Xin and Todisco, Massimiliano and Sahidullah, Md and Patino, Jose and Nautsch, Andreas and Liu, Xuechen and Lee, Kong Aik and Kinnunen, Tomi and Evans, Nicholas and Delgado, H{\'{e}}ctor},
booktitle = {Proc. ASVspoof Challenge workshop},
doi = {10.21437/ASVSPOOF.2021-8},
pages = {47--54},
title = {{ASVspoof 2021: accelerating progress in spoofed and deepfake speech detection}},
year = {2021}
}


@inproceedings{Todisco2019,
author = {Todisco, Massimiliano and Wang, Xin and Vestman, Ville and Sahidullah, Md. and Delgado, H{\'{e}}ctor and Nautsch, Andreas and Yamagishi, Junichi and Evans, Nicholas and Kinnunen, Tomi H and Lee, Kong Aik},
booktitle = {Proc. Interspeech},
doi = {10.21437/Interspeech.2019-2249},
pages = {1008--1012},
title = {{ASVspoof 2019: future horizons in spoofed and fake audio detection}},
year = {2019}
}

