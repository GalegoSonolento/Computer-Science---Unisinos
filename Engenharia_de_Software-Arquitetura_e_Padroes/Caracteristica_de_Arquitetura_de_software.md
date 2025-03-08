# Restrição Operacional (Operational Constraint)

Constraints define the contractual behavior of an operation, what must be true before they are called (pre-conditions) and what is true after they are called (post-conditions). In this respect they are related to the State model of a Class and can also relate to the guard conditions that apply to a transition. You can define both pre- and post- conditions for an operation.
**https://sparxsystems.com/enterprise_architect_user_guide/17.0/modeling_fundamentals/operationconstraints.html**

In software architecture design, constraints come in two basic flavors - technical and business.  On most projects there are only a handful of constraints, but these constraints are a highly influential architectural driver.  Constraints, as the dictionary definition above indicates, are a limiting factor and severely restrict options for making design decisions.  They are also fixed design decisions that cannot be changed and must be satisfied.  You could think of constraints as the ultimate non-negotiable, "must have" requirement.  It is for this reason that architecture design constraints must be created and accepted with care.

Technical Constraints
Technical constraints are fixed technical design decisions that absolutely cannot be changed.  Most often technical constraints are provided by stakeholders (perhaps after some digging) at the outset of the project. Sometimes a team may choose to create a constraint, perhaps to simplify the world in which they are working.  Regardless of the origin, these architecture drivers are technical in nature and are considered unchangeable and indeed very soon become so.
Use of a specific library or framework 
Operating system or platforms supported 
Programming language

Business Constraints
Business constraints are unchangeable business decisions that in some way restrict the software architecture design.  Business constraints are similar to technical constraints in that they are decisions that cannot be changed, but rather than influencing structures directly through technology, the influence occurs indirectly through business decisions.  It might be easiest to discuss some examples.
Schedule 
Budget 
Team composition and make-u
Software licensing restrictions or requirements

It's common that quality attributes and functional requirements will be offered up as constraints. It is a huge mistake to treat a quality attribute as a constraint, even one that is extremely high priority. Quality attributes are NEVER constraints.
**https://www.neverletdown.net/2014/10/dealing-with-constraints-in-software-architecture.html**

Restrição operacional, na definição do termo, se refere à um limite ou requerimento de uma determinada operação, que não será mais alterado no decorrer do projeto (ou, caso seja, será bastante custoso) e determinam o comportamento operacional e contratual de uma arquitetura. Essas restrições devem ser cuidadosamente analisadas e ponderadas antes de serem admitidas e definidas para um projeto, dado que serão requisitos não-negociáveis e absolutamente necessários para que o sistema pare em pé.
Seja para limitar o escopo, facilitar a vida dos projetistas/arquitetos, ou satisfazer as vontades do contratante, Restrições Operacionais aparecem de duas maneiras: 1) restrições técnicas (linguagem de programação, SO suportado, framework/library, etc) e 2) burocráticas (composição de time, licença de software utilizada, orçamento, etc).
Restrições operacionais podem se referir (e algumas vezes vão) à requisitos do sistema. Todavia, não confunda com os requisitos qualitativos; esses nunca devem ser misturados com as restrições abordadas aqui.