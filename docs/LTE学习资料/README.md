# LTE 自学指南

> LTE（Long Term Evolution，长期演进）是 3GPP（3rd Generation Partnership Project，3G 伙伴项目）组织制定的一种移动通信标准，与 2G 和 3G 相比，具有速率更快、容量更大以及覆盖范围更大等特点，是目前主流的移动通信技术。LTE 实施了核心网的全 IP 化以及核心网与无线网络接口的 IP 化，并且还去掉了 WCDMA 网络中的 CS（Circuit Switching，电路交换）域设备，只保留了 PS（Packet Switching，分组交换）域设备，使核心网的架构得到了大幅度的精简。随着无线通信技术的不断发展，LTE 在全球范围内得到了大规模的部署，并成为了人们日常生活中必不可少的一部分。
>

该目录记录了本人在硕士期间学习 LTE 的过程中查阅过的专业书籍、标准协议、论文以及开源代码，并且包含了自己整理的一份 LTE 学习笔记，其中囊括了自己对 LTE 协议以及开源 SDR 项目源码的理解。

## 入门书籍

- 《LTE 教程：原理与实现》
- 《LTE 教程：结构与实施》
- 《LTE 教程：机制与流程》
- 《LTE 教程：业务与信令》

## 标准协议

EPC 常用协议及其描述：

- TS 23.002: gives an overview the architecture of the 3GPP system. In particular, it describes all the network elements used in the EPC and also in legacy core networks.
- TS 23.401: defines the architecture of the EPC for E-UTRAN access.
- TS 23.402: defines the architecture enhancements for non-3GPP accesses.
- TS 24.008: defines inter-system mobility between LTE and 2G/3G.
- TS 24.301: defines the protocol details of the NAS.
- TS 24.303: defines inter-system mobility between LTE and non-3GPP accesses.

E-UTRAN 常用协议及其描述：

- TS 36.300: Evolved Universal Terrestrial Radio Access (E-UTRA) and Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Overall description; Stage 2.
- TS 36.304: Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) procedures in idle mode.
- TS 36.321: Evolved Universal Terrestrial Radio Access (E-UTRA); Medium Access Control (MAC) protocol specification.
- TS 36.322: Evolved Universal Terrestrial Radio Access (E-UTRA); Radio Link Control (RLC) protocol specification.
- TS 36.323: Evolved Universal Terrestrial Radio Access (E-UTRA); Packet Data Convergence Protocol (PDCP) specification.
- TS 36.331: Evolved Universal Terrestrial Radio Access (E-UTRA); Radio Resource Control (RRC); Protocol specification.

> 所有 LTE 的相关协议均可以在 [3GPP – The Mobile Broadband Standard](https://www.3gpp.org/) 上进行下载。

## 开源项目

- [OpenAirInterface – 5G software alliance for democratising wireless innovation](https://openairinterface.org/)
- [OpenLTE (sourceforge.net)](https://openlte.sourceforge.net/)
- [srsLTE (github.com)](https://github.com/srsLTE/)
- [srsRAN Project - Open Source RAN (srslte.com)](https://www.srslte.com/)
