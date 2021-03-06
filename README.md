甲基化生信分析pipeline – 甲基化测序的一键自动生信分析流程
=======================================
## 甲基化基本概念：
[甲基化概念](https://www.thermofisher.cn/cn/zh/home/life-science/epigenetics-noncoding-rna-research/methylation-analysis-.html)
## 下载公共数据库GEO的甲基化测序数据：
[GEO甲基化数据](https://www.ncbi.nlm.nih.gov/gds/?term=methylation>)
## 项目介绍：
#### 甲基化市面开源软件繁多且分析方法成熟，但可用的一键分析pipeline不多，多数为零散代码块。本项目提供一键迁移部署甲基化分析pipeline，在Linux环境上运行，作者会定期维护更新function
## 主要功能：
-    质量控制-fastp
-    甲基化reads比对-bismark
-    甲基化位点提取-DMRfinder
-    样本PCA投影测量距离-FactoMineR
-    甲基化位点Manhattan图-qqman
-    十等分统计甲基化位点检测-自行开发
-    组间差异甲基化分析-DSS
-    甲基化基因的volcano plot-EnhancedVolcano
-    甲基化基因的heatmap plot-pheatmap
-    发送状态代码到API-request
## 主要依赖：
#### python>=3.0.0：
-    os
-    sys
-    re
-    time
-    subprocess
-    requests
-    pathlib
-    pandas
-    numpy
-    shelve
-    math
-    pymysql
-    matplotlib
#### R>=3.6.0:
-    qqman
-    EnhancedVolcano
-    pheatmap
-    FactoMineR
-    factoextra
-    DSS
-    bsseq
## 示例程序：
    python methylation.py /home/DUAN/methyl_rawdata/yinle/293FT_1.fq.gz,/home/DUAN/methyl_rawdata/yinle/293FT_2.fq.gz~/home/DUAN/methyl_rawdata/yinle/293FT-HOSK_1.fq.gz,/home/DUAN/methyl_rawdata/yinle/293FT-HOSK_2.fq.gz~/home/DUAN/methyl_rawdata/yinle/J-H-0_1.fq.gz,/home/DUAN/methyl_rawdata/yinle/J-H-0_2.fq.gz~/home/DUAN/methyl_rawdata/yinle/J-H-5_1.fq.gz,/home/DUAN/methyl_rawdata/yinle/J-H-5_2.fq.gz~/home/DUAN/methyl_rawdata/yinle/J-H-10_1.fq.gz,/home/DUAN/methyl_rawdata/yinle/J-H-10_2.fq.gz 293FT,293FT-HOSKDUANJ-H-0,J-H-5,J-H-10 /public/mlrna_seq/sample_result/16/ 16
#### 样品间请使用fastq路径串联由逗号分割，表示分组信息请用DUAN分割组间信息，组内使用逗号分割
## 部分运行结果展示：
![img](https://gitee.com/duangao/methylation/raw/master/sample_result/heatmap.png)
![img](https://gitee.com/duangao/methylation/raw/master/sample_result/manhattan.png)
![img](https://gitee.com/duangao/methylation/raw/master/sample_result/slice.png)
![img](https://gitee.com/duangao/methylation/raw/master/sample_result/volcano.png)

    
    
    


