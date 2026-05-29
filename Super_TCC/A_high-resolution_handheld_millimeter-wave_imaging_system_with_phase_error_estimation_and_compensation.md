# A_high-resolution_handheld_millimeter-wave_imaging_system_with_phase_error_estimation_and_compensation
- Nesse artigo a ideia era justamente baratear um processo e aparelho para ser handheld (mmWave e SAR)

# Introduction
- aparelho handheld MIMO compliant e SAR com equipamento off-the-shelf
- *Based on these findings, we focus on the direction most susceptible to motion errors and estimate the optimal PSF based on the quadratic feature of the ideal phase history. Once obtaining the estimated PSF, we can derive and compensate for the phase errors caused by manual scanning and reconstruct the target with the efficient frequency-domain imaging method*

# Methods
- planos 2D são usados pra montagem do espaço 3D das mmWaves
- os problemas atuais geralmente caem no modelo mostrando uma imagem do SAR desfocada

# Implementation details
- *Notably, in this paper, a linear array is employed to facilitate MIMO SAR imaging. Hence, at each time step i, there will be multiple phase variations corresponding to multiple antennas. Although it is possible to estimate the phase error for each antenna, such an approach would increase computational costs and exacerbate the impact of incorrect estimations*
- existe um scanner digital mesmo com as ondas e tals
    - mas ainda existe uma implementação física

# Results
- São resultados bastante interessantes inclusive
- o scanner passa como se fosse um scanner comum mesmo, esquerda para direita e vice-versa na linha de baixo
- inclusive o sistema ainda consegue ler por trás de alguns materiais, como no exemplo da tesoura
- o modelo ainda precisa de algum pós-processamento
- esse modelo ainda usa um ponto de referência pra cálculo de margem de erros
- o scanner macânico normalmente tem mais nitidez, mas mata o fato de ser handheld

# Data availability
- dados disponíveis com o autor

# Code availability
- códigos disponíveis com o autor