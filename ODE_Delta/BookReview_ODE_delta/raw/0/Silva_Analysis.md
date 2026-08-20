# Silva (Editor), Montalvão e Silva & Pina da Silva - "Vibration and Wear in High-Speed Rotating Machinery"

## Framework Classification
**Framework 45 - Applied Rotor Dynamics and Bearing Behavior in Rotating Machinery**

**Type**: NATO Advanced Study Institute (ASI) Proceedings - Edited Volume
**Editors**: J. M. Montalvão e Silva & F. A. Pina da Silva (CEMUL, Lisbon Institute of Technology)
**Publisher**: Kluwer Academic Publishers
**ISBN**: 978-94-010-7354-7
**Publication Year**: 1990
**Total Pages**: 829
**Conference**: NATO ASI on "Vibration and Wear Damage in High Speed Rotating Machinery"
**Venue**: Troia, Setúbal, Portugal
**Date**: April 10-22, 1989

---

## 1. CENTRAL MISSION AND UNIQUE CONTRIBUTION

The **Silva collection** is a multidisciplinary NATO Advanced Study Institute proceedings that bridges the traditionally separate fields of **tribology** (wear and lubrication) and **rotor dynamics** (vibration analysis) in the context of high-speed rotating machinery.

**Core Mission**:
- Establish communication between tribologists and dynamicists
- Address condition monitoring of rotating machines combining both wear and vibration perspectives
- Provide state-of-the-art treatment of rotor-bearing system dynamics including nonlinear effects
- Document practical engineering approaches to bearing behavior, instability, and failure prediction
- Integrate theoretical analysis with experimental validation and practical maintenance strategies

**Unique Contribution**:
- **Interdisciplinary Framework**: One of the few comprehensive treatments combining tribology + dynamics
- **Nonlinear Effects**: Detailed treatment of oil-whirl instability, squeeze-film dampers, and bearing nonlinearities
- **Practical Applications**: Focus on real turbomachinery, steam turbines, pumps, compressors
- **Modal Testing**: Connection between theoretical analysis and experimental identification
- **Condition Monitoring**: Integration of wear debris analysis with vibration signature analysis

---

## 2. TREATMENT OF DISCONTINUITIES ON THE RIGHT-HAND SIDE

### 2.1 Matrix Equation Formulation

**Primary Model** (Chapter: "Vibration of Rotor-Bearing Assemblies" by R. Holmes, Page 280):

```
M Ẍ + C X + K X = F(t)
```

where:
- M = symmetric mass matrix
- C = **non-symmetric** damping matrix
- K = **non-symmetric** stiffness matrix
- X = displacement vector
- F(t) = forcing vector

**Critical Feature**: Both C and K matrices contain **skew-symmetric (non-conservative) components**.

### 2.2 Sources of Discontinuities and Non-Symmetries

The book systematically addresses several physical phenomena that introduce discontinuities:

#### A. Gyroscopic Effects (Page 280-281)

**Effect**: Rotating rotor polar moment J creates gyroscopic moments orthogonal to angular velocity vector ω.

**Mathematical Representation** (Equation 2, Page 280):
```
I[θ̈ₓ]     Jω[0   -1][θ̇ₓ]     S[1  0][θₓ]
  [θ̈ᵧ]  +    [1    0][θ̇ᵧ]  +   [0  1][θᵧ] = 0
```

**Key Property**: 
- Skew-symmetric component (gyro moment) in C matrix: [0  -1; 1  0]
- This is **conservative** despite being in C matrix (unusual!)
- Results in **bifurcation** of natural frequencies (equation 4, page 281):
  ```
  ω_{n1,n2} = (Jω/2I)[1 ± √(1 + 4I²S²/(Jω)²)]
  ```

#### B. Internal Damping - Energy Addition (Pages 281-282)

**Physical Model**: Flexible shaft with viscous internal damping; mass suspended elastically.

**Critical Discontinuity**: When shaft rotates supercritically (mass orbits slower than ring), viscous drag **pulls mass forward** and **adds energy** to orbit.

**Mathematical Form** (Equation 5, Page 281):
```
m ẍ + a·x + (b/a)ω · ẏ = 0
m ÿ + a·y - (b/a)ω · ẋ = 0
```

**Instability Threshold**:
- Instability occurs when: ω > √(a/m) = ω_n
- Instability frequency: also at ω_n (same as undisturbed natural frequency)
- External damping delays onset but does NOT prevent instability

**Physical Interpretation**: 
- The term `(b/a)ω` represents **velocity-dependent cross-coupling**
- Creates **self-excited vibration** — system pumps its own energy into vibration
- **Discontinuity**: System transitions from damped to unstable at critical speed

#### C. Oil-Whirl Instability in Journal Bearings (Pages 283-285)

**Most Important Practical Discontinuity**: 

The journal bearing's oil film exhibits **highly nonlinear stiffness and damping** that changes discontinuously with:
- Loading direction
- Shaft eccentricity
- Rotational speed
- Cavitation conditions

**Oil-Film Force Components** (Equations 6-7, Pages 284-286):

For a **full 360° flooded bearing** (Equation 6):
```
[Fₓ]   = [0      aω/2][y]   + [b    0][ẏ]
[Fᵧ]     [-aω/2   0   ][x]     [0    b][ẋ]
```

**Key Features**:
1. **Direct stiffness vanishes**: Only cross-stiffness (aω/2) remains
2. **Only direct damping exists**: Only b along velocity direction
3. **Cross-coupling coefficient**: a/b = ω/2

**Bifurcation of Response** (Page 284):
- At low speed: stable circular whirl motion
- As speed increases: oil wedge geometry changes
- At critical speed ≈ 2ω_n: **oil-whirl instability onset**
- Above critical: forward whirl at ω/2 frequency

**Physical Mechanism** (Figure 2, Page 283):
1. External load W deflects journal ↓
2. Hydrodynamic pressure P builds in converging wedge
3. Oil dragged at ≈ ω/2 average velocity
4. If journal center orbits at ω/2, wedge moves away from oil
5. **Instantaneous loss of load-carrying capacity**
6. Journal goes unstable in forward-whirling motion

**Discontinuity Type**: **Bifurcation with hysteresis**
- Stable for ω < ω_critical
- Becomes unstable at ω = ω_critical
- Nonlinearity limits amplitude to bearing clearance circle

#### D. Annular Clearance Seals (Pages 286-287)

**Similar to Bearings**: Seals in pumps and compressors produce **similar destabilizing cross-stiffness forces**:

```
Hydraulic force ≈ (2aω/π)·y - (dx/dt)·(aω/π)

Skew-symmetric K-matrix: [0      aω/(2π)  ]
                         [-aω/(2π)   0    ]
```

**Destabilization Threshold**: ~half running speed, similar to oil-whirl

### 2.3 Decomposition into Symmetric and Skew-Symmetric Parts (Pages 287-288)

**Key Mathematical Technique**:

```
C = Cs + Css    (symmetric + skew-symmetric parts)
K = Ks + Kss
```

where:
- Cs = (C + Cᵀ)/2  → Conservative (yields positive energy dissipation)
- Css = (C - Cᵀ)/2 → Non-conservative (can add or remove energy)
- Ks = (K + Kᵀ)/2  → Symmetric stiffness (restoring forces)
- Kss = (K - Kᵀ)/2 → Anti-symmetric stiffness (destabilizing)

**Physical Meaning**:
- Css can be associated with **gyroscopic moments** (energy-neutral)
- Kss represents **cross-stiffness forces** that couple orthogonal directions
- These non-conservative components are **unique to rotating systems**

### 2.4 Discontinuity Characteristics

**Types of Discontinuities Addressed**:

1. **Bifurcations**: Natural frequencies split (gyroscopic effect)
2. **Threshold Phenomena**: System behavior changes abruptly at critical speed
3. **Hysteresis**: Instability depends on acceleration/deceleration direction
4. **Nonlinear Saturation**: Amplitude limits due to bearing clearances, nonlinear stiffness
5. **Cavitation Events**: Discontinuous loss of bearing load capacity
6. **Squeeze-Film Effects**: Highly nonlinear damper response (page 293)

**All These Are Treated as Embedded in Matrix Equations** — Not as explicit delta function forcing.

---

## 3. IMPULSE RESPONSE AND TRANSIENT ANALYSIS

### 3.1 Modal Analysis and Impulse Testing

**Reference**: Chapters on "Modal Testing Techniques" and "Applications of Modal Testing" by D. J. Ewins (Pages 299-337)

**Impulse Response in Modal Context**:
- **Impulse Excitation**: Strike a structure with calibrated hammer
- **Response Measurement**: Accelerometer records transient response
- **Frequency Response**: FFT of impulse → transfer function H(jω)

**Standard Second-Order System Response** (from Chapter 3.1 of Duffy reference, implicit here):
```
h(t) = G(s) impulse response
     = inverse Laplace{H(s)}
```

**Application to Rotor Testing** (Page 299-323):
- Modal testing provides experimental validation of theoretical rotor models
- Identifies damping ratio and natural frequencies
- Separates modes of vibration (forward whirl vs. backward whirl)
- Detects nonlinearities through harmonic distortion in impulse response

### 3.2 Rotor System Response to Transient Disturbances

**Reference**: Rotor-Bearing Assemblies chapter (Pages 279-296)

**Key Finding**: Response near critical speed shows **nonlinear saturation** (Page 290):

When threshold speed is exceeded:
- Shaft becomes unstable with precession frequency f = ω/2
- Amplitude grows nonlinearly
- Eventually reaches bearing clearance circle → limit cycle
- Amplitude remains bounded (unlike linear instability theory)

**Transient Response Characteristics**:
1. **Stable region**: Response decays exponentially with natural damping
2. **Borderline**: Log decrement approaches zero (marginal stability)
3. **Unstable region**: Oscillation amplitude grows, reaches limit cycle
4. **Complex dynamics**: Multiple frequencies present (1× running speed, precession frequency, etc.)

### 3.3 Connection to Initial Condition Changes

**Reference**: System identification chapter (Page 527+)

**Not Explicitly Addressed**: The book does NOT discuss equivalence between impulsive forcing and initial condition jumps in the classical sense (Pleshkov/Samoilenko framework).

**However, Implicitly Present**:
- Modal testing assumes zero initial conditions, system excited by impulse
- Response characterizes system properties independent of excitation history
- State-space realization connects impulse response to state transition matrix

---

## 4. EQUIVALENCE: DISCONTINUOUS FORCING ↔ INITIAL CONDITION JUMPS

### 4.1 Not Primary Focus

Unlike the Duffy framework (Green's functions) or Pleshkov (algorithmic synthesis), the Silva collection does **NOT explicitly address** the mathematical equivalence between:
- Impulsive forcing δ(t - τ)
- Jump conditions in state variables x(τ⁺) - x(τ⁻)

### 4.2 Implicit Physical Equivalence

**However**, several chapters implicitly rely on this equivalence:

**In Bearing Dynamics** (Page 286):
- Bearing stiffness coefficients axx, axy, ayx, ayy describe **initial displacement-force relationship**
- Cross-stiffness (axy) creates coupling: force in x-direction produces displacement in y-direction
- This is structurally similar to initial condition coupling via impulse

**In Modal Testing** (Page 299+):
- Hammer strike imparts initial velocity to structure
- This is equivalent to imposing initial condition v(0) = velocity spike
- Response depends only on system properties and this initial condition

**In Rotor-Bearing Interaction** (Page 286):
When system becomes unstable:
```
Small disturbance at t = 0 → Initial condition x(0) = δ
→ Exponential growth with frequency ω_n
```

This is mathematically equivalent to:
```
Impulse F(t) = δ(t) at t = 0
→ Response h(t) = G(s) × impulse
→ Same exponential growth
```

---

## 5. HIERARCHICAL POSITION RELATIVE TO OTHER APPROACHES

### 5.1 Scope and Focus

**Strengths**:
1. **Practical Engineering Focus**: Real turbomachinery, not academic examples
2. **Nonlinear Phenomena**: Oil-whirl, squeeze-film dampers, bearing cavitation
3. **Interdisciplinary**: Combines tribology, dynamics, condition monitoring, and life assessment
4. **Experimental Validation**: Modal testing, bearing testing, full-scale machine measurement
5. **Bearing Dynamics**: Most comprehensive treatment of oil-film bearing instability
6. **Applied Methods**: Fault diagnosis, remaining life prediction, bearing selection

**Limitations**:
1. **Not Mathematical Theory**: Focuses on applications, not rigorous theory
2. **Linear Around Operating Point**: Linearizes about equilibrium for stability analysis
3. **No Distribution Theory**: Does not use Schwartz distributions or measure-theoretic framework
4. **Primarily Rotor-Bearing Systems**: Specialized to rotating machinery, not general ODE theory
5. **No Filippov or Differential Inclusions**: No treatment of multivalued RHS

### 5.2 Relationship to Other Frameworks

**Compared to Duffy (Framework 44 - Green's Functions)**:
- **Duffy**: Theoretical foundations; impulse response for linear ODE
- **Silva**: Applied rotor dynamics; nonlinear bearing effects; practical instability prediction
- **Hierarchy**: Duffy provides theory, Silva provides applications to real machines
- **Complementary**: Duffy explains *how* to compute impulse response; Silva shows *where* it matters in bearings

**Compared to Samoilenko-Perestyuk (Framework 32)**:
- **Samoilenko-Perestyuk**: Impulsive differential equations; multiple solution concepts; sliding modes
- **Silva**: Rotor dynamics with nonlinear bearing forces; no explicit impulse effects
- **Relation**: Silva's oil-whirl bifurcation is a special case of nonlinear ODE; Samoilenko-Perestyuk more general

**Compared to Filippov (Framework 6)**:
- **Filippov**: Discontinuous RHS; multiple solution concepts; sliding mode theory
- **Silva**: Nonlinear continuous RHS (bearings); no discontinuities in classical sense
- **Relation**: Silva's bearing forces are nonlinear but continuous; Filippov addresses discontinuous RHS

**Compared to Kiseleva (Framework 40 - Differential Inclusions)**:
- **Kiseleva**: Multivalued RHS; drilling systems with discontinuous friction
- **Silva**: Single-valued but nonlinear bearing forces
- **Relation**: Kiseleva more general (multivalued); Silva specialized to rotor-bearing coupling

**Compared to Yang (Framework 37 - Impulsive Control)**:
- **Yang**: Impulsive control; state jumps at discrete times; stability via Lyapunov
- **Silva**: Bearing instability; continuous dynamics; self-excited vibrations
- **Relation**: Yang addresses *designed* impulses for control; Silva addresses *parasitic* instabilities

**Compared to Pleshkov (Framework 33 - Algorithmic Synthesis)**:
- **Pleshkov**: Impulse ↔ IC jump equivalence; formula 3.3 for n-th order systems
- **Silva**: Implicit equivalence in bearing dynamics; practical rather than algorithmic
- **Relation**: Pleshkov shows mathematical equivalence; Silva demonstrates physical manifestation

### 5.3 Position in Hierarchical Framework

**Proposed Classification Level**:
- **Level 2-3 (Theory-Practice Bridge)**

**Justification**:
- Builds on linear rotor theory (Duffy, classical vibration theory)
- Adds nonlinear bearing behavior (beyond Duffy)
- Precedes specialized applications (impulsive control, grinding systems)
- Widely used reference in turbomachinery engineering
- Represents state-of-practice in bearing instability analysis (1989)

---

## 6. NONLINEAR PHENOMENA AND DISCONTINUOUS BEHAVIOR

### 6.1 Oil-Whirl Instability - The Central Nonlinearity

**Most Important Result** (Pages 283-294):

The **oil-whirl instability** is a classic example of **self-excited vibration** arising from nonlinear bearing behavior.

**Threshold Speed Calculation** (Page 289-291):

Using **dynamic stiffness matching**:
```
Unstable when: |Z_rotor| intersects k_bearing

Where Z_rotor = dynamic stiffness of rotor half-system
      k_bearing = effective stiffness of bearing oil-film
```

**Typical Threshold**: ~2 × first natural frequency ω_n

**Response Behavior**:
- Below threshold: Damping stabilizes system
- At threshold: Critical instability (incipient whirl)
- Above threshold: **Nonlinear saturation to limit cycle**

### 6.2 Squeeze-Film Dampers - Highly Nonlinear Elements (Page 293)

**Application**: Damping ring between bearing outer race and housing

**Nonlinear Characteristics**:
1. **Velocity-dependent stiffening**: As vibration amplitude increases, effective stiffness changes
2. **Multiple resonances**: At frequencies ≈ 2ω_n, 3ω_n, 4ω_n ... due to subharmonic response
3. **Frequency-dependent damping**: Not constant with frequency
4. **Cavitation effects**: If emptied of oil, introduces impulsive forces

**Mathematical Challenge**: 
- Cannot use linear analysis near squeeze-film
- Nonlinear differential equations required
- Requires continuation methods or numerical simulation

### 6.3 Cavitation and Load-Loss Discontinuity (Page 283-284)

**Physical Phenomenon**:
- When journal speed matches oil-wedge speed (ω/2), converging wedge **moves away from oil**
- Hydrodynamic pressure drops → oil cavitates (vapor bubbles form)
- **Instantaneous loss of load-carrying capacity**
- Bearing can no longer support journal

**Mathematical Representation**:
- This is a **discontinuity in bearing force**
- Can be modeled as:
  - Piecewise smooth: F = F₁ if eccentricity < ε_crit; F = F₂ otherwise
  - Or: Discontinuous jump in bearing coefficients when cavitation occurs

**Not Addressed**: Silva does not use delta function representation; treated as nonlinear phenomenon

---

## 7. CONDITION MONITORING AND FAULT DETECTION

### 7.1 Wear Debris Analysis (Pages 1-72)

**Part I of Silva**: "Particle and Wear Debris Analysis"

**Connection to Impulse Response**:
- Wear particles originate from **impulsive contact events** between surfaces
- Each microscopic impact = impulse in contact mechanics
- Accumulated wear = integral of impulse responses over operating time
- Debris particle size/shape encodes information about **impact force and duration**

**Example** (Pages 11-15):
- Ball bearing particle (Figure 5): Spherical wear debris from fatigue spalling
  - Spalling = sudden loss of surface material under stress
  - Each spall = micro-impulse releasing stress energy
  - Particle shape reveals impulse characteristics (brittle vs. ductile failure)

**Implications for Discontinuous Systems**:
- Bearing wear = result of repeated impulsive contacts
- Wear rate accelerates when bearing enters unstable regime (oil-whirl)
- Debris analysis predicts bearing failure before catastrophic break

### 7.2 Vibration Signature Analysis (Pages 221-242)

**Connection to Impulse Response**:
- Machine vibration signature = system's response to all internal impulses
- Bearing defects produce **periodic impulsive forcing** (spall hits rolling elements)
- Gear mesh impacts = periodic impulses with phase modulation
- Turbine blade flutter = aerodynamic impulses

**Key Diagnostic Features**:
1. **Synchronous vibration** (1× running speed): Rotor imbalance (continuous forcing)
2. **Subsynchronous** (0.4-0.5× running speed): Oil-whirl instability (our concern!)
3. **Higher harmonics** (2×, 3×, ...): Bearing defects, gear mesh
4. **Broadband noise**: Cavitation, friction instability

**Interpretation**:
- Subsynchronous component = precession frequency = ω/2
- Indicates oil-whirl instability in journal bearings
- Encoded in vibration signature as impulse response characteristic

### 7.3 Expert System Approach (Pages 759-804)

**Reference**: Chapters on "Intelligent Knowledge Based System for Fault Diagnosis" and "Remaining Life Evaluation"

**Methodology**:
1. Map measured vibration signature to known fault signatures
2. Use modal parameters (natural frequencies, damping) from modal testing
3. Cross-reference with bearing type, operating speed, temperature
4. Predict remaining life from rate of change of vibration amplitude

**Role of Impulse Response Knowledge**:
- System signatures are essentially impulse responses to bearing defects
- Damping changes with bearing degradation
- Natural frequency shifts indicate clearance changes
- These are encoded in measured impulse response via modal testing

---

## 8. MATHEMATICAL RIGOR AND LIMITATIONS

### 8.1 Rigorous Elements

**Well-Posed Rotor Dynamics Theory**:
- Matrix equation formulation (Equation 1, Page 280)
- Stability analysis via characteristic equation and Routh-Hurwitz criterion (Page 296)
- Modal decomposition and frequency response analysis
- Experimental validation via modal testing

**Physical Mechanism Explanations**:
- Oil-whirl phenomenon clearly explained via wedge mechanics (Figure 2, Page 283)
- Energy analysis of instability (Page 281: "viscous drag pulls mass forward")
- Threshold speed prediction via dynamic stiffness matching (Pages 288-289)

**Empirical Validation**:
- Experimental recordings of oil-whirl instability (Figure 3, Page 282)
- Actual rotor measurements showing bifurcation to second mode (Figure 6, Page 290)
- Bearing type comparison (Figure 7, Page 292)

### 8.2 Limitations

**1. Linearization Around Operating Point**:
- Bearing forces linearized: axx, axy, bxx, bxy are **constant coefficients**
- Valid only for small perturbations around equilibrium
- Large-amplitude vibrations invalidate linear analysis

**2. No Rigorous Discontinuity Theory**:
- Cavitation treated phenomenologically, not mathematically
- No delta function representation of bearing force discontinuities
- No measure-theoretic framework

**3. Limited to Circular Orbits**:
- Assumes journal precesses in circular orbit
- Actual motion can be complex, with cusps and multiple loops
- Squeeze-film response produces n-lobed orbits (noted but not analyzed rigorously)

**4. No Formal Stability Certificates**:
- Uses heuristic frequency response approach (log decrement)
- No Lyapunov function analysis
- Bifurcation theory mentioned informally but not rigorously applied

**5. Bearing Coefficient Identification**:
- Book assumes bearing coefficients axx, axy, etc. are **known**
- In practice, these must be identified from experiments (Chapter on "Identification of Stiffness, Damping and Inertia Coefficients", Page 507)
- Identification is inverse problem with uniqueness issues

---

## 9. KEY MATHEMATICAL EQUATIONS

### 9.1 Gyroscopic Bifurcation (Equation 4, Page 281)

```
ω_{n1,n2} = (Jω/2I)[1 ± √(1 + 4I²S²/(Jω)²)]
```

**Interpretation**:
- For J >> I: Two forward/backward whirl frequencies
- For I >> J: Forward whirl at ~synchronous, backward at ~zero
- Bifurcation due to skew-symmetric gyroscopic term

### 9.2 Oil-Film Force Representation (Equation 7, Page 286)

```
[Fx]   [axx  axy] [x]   [bxx  bxy] [ẋ]
[Fy] = [ayx  ayy] [y] + [byx  byy] [ẏ]
```

**Special Case - Full 360° Flooded Bearing** (Page 284):
```
[Fx]   [0      aω/2] [y]   [b   0] [ẏ]
[Fy] = [-aω/2   0  ] [x] + [0   b] [ẋ]
```

- Direct stiffness vanishes (axx = ayy = 0)
- Cross-stiffness proportional to running speed ω
- Only direct damping b exists

### 9.3 Instability Threshold (Page 296)

```
ω_instability > ω_n = √(a/m)
```

**Frequency of Instability**:
```
f_instability = ω_instability / 2 ≈ ω_n
```

This is why **subsynchronous (½ running speed) vibration indicates bearing instability**.

### 9.4 Dynamic Stiffness Matching (Page 288)

```
Z(ω) = P(ω)/X(ω)  [rotor half-system]
k(ω)              [bearing oil-film]

Resonance when: Real(Z) + Real(k) = 0
```

This graphical method predicts instability threshold.

---

## 10. COMPARISON TABLE: SILVA VS. RELATED FRAMEWORKS

| Aspect | Silva | Duffy | Samoilenko-P. | Filippov |
|--------|-------|-------|----------------|----------|
| **Focus** | Rotor-bearing dynamics | ODE theory | Impulsive DE | Discontinuous RHS |
| **Oil-whirl** | Central topic | Not addressed | Related (nonlinear) | Possible application |
| **Impulse Response** | Via modal testing | Theoretical definition | Component | Not primary |
| **Nonlinearity** | Central (bearings) | Not treated | Implicit | Explicit (RHS) |
| **Stability** | Via frequency response | Via Laplace analysis | Via Lyapunov | Via Filippov theory |
| **Applications** | Turbomachinery | General linear ODE | Mechanics | Control systems |
| **Cavitation** | Addressed | Not addressed | Not addressed | Not addressed |
| **Practical** | Highly practical | Theoretical | Mixed | Mixed |

---

## 11. RELEVANCE TO LITERATURE REVIEW

### 11.1 HIGH RELEVANCE

**Strong Connections**:
1. **Rotor Dynamics**: Core application of vibration theory to machinery
2. **Bearing Instability**: Nonlinear phenomenon requiring discontinuous analysis
3. **Modal Testing**: Experimental impulse response extraction
4. **Damping Effects**: Oil-film damping as self-exciting mechanism
5. **Nonlinear Saturation**: Limit cycles from nonlinear bearing forces

### 11.2 MODERATE RELEVANCE

**Secondary Connections**:
1. **Condition Monitoring**: Wear particles encode impulse history
2. **Stability Theory**: Bifurcation and threshold phenomena
3. **System Identification**: Extracting bearing coefficients from response data

### 11.3 LIMITED RELEVANCE

**Not Directly Addressing**:
1. **Delta Function Formalism**: No distribution theory treatment
2. **Filippov Sliding Modes**: Not discussed
3. **Differential Inclusions**: Not addressed
4. **Impulsive Control**: Not a control system application

---

## 12. SPECIFIC CHAPTERS RELEVANT TO IMPULSE/DISCONTINUITY

| Chapter Title | Author(s) | Pages | Relevance | Key Topic |
|--------------|-----------|-------|-----------|-----------|
| "Vibration of Rotor-Bearing Assemblies" | R. Holmes | 279-296 | **HIGH** | Oil-whirl instability, gyroscopic effects |
| "Critical Speeds of Continuous Shaft-Disc Systems" | M. Sabuncu, A. Kaşar | 241-252 | MODERATE | Shaft dynamics, resonance |
| "Modal Testing Techniques" | D. J. Ewins | 299-310 | MODERATE | Impulse excitation, frequency response |
| "Applications of Modal Testing" | D. J. Ewins | 311-322 | MODERATE | Experimental impulse response |
| "On Bearing Deformation and Temperature Distribution" | R. Holmes | 385-398 | MODERATE | Bearing load distribution |
| "The Control of Rotor Vibration Using Squeeze-Film Dampers" | R. Holmes | 399-412 | MODERATE | Nonlinear damping, amplitude control |
| "Dynamic Behaviour of Hydrostatic Radial Bearings" | M. Vermeulen | 455-470 | MODERATE | Different bearing type with pressure forces |
| "Identification of Stiffness, Damping Coefficients of Annular Turbulent Seals" | R. Nordmann | 507-526 | MODERATE | Bearing coefficient extraction |
| "The Effect of Translational Bearing Misalignment on Response and Stability" | P. J. Ogrodnik et al. | 547-558 | LOW | Bearing nonlinearity due to misalignment |
| "Destabilization of Rotors from Friction in Internal Joints" | I. W. Lund | 617-629 | LOW | Different destabilization mechanism |
| "Particles in Lubricating Oils" | E. Jantzen | 1-12 | LOW | Wear debris, not dynamics |

---

## 13. CONCLUSION

**Silva's "Vibration and Wear in High-Speed Rotating Machinery"** is a **key reference for applied rotor dynamics** and represents the **state-of-practice in bearing behavior and machinery condition monitoring** (1989 NATO ASI conference).

**Core Contribution**:
1. **Practical theory** of oil-whirl instability in journal bearings
2. **Nonlinear phenomena** in rotor-bearing systems
3. **Experimental modal testing** for validation
4. **Condition monitoring** integration of vibration + wear
5. **Expert system approaches** for fault diagnosis

**Position in Hierarchy**:
- **Level 2-3 (Theory-Practice Bridge)** — Between foundational theory (Duffy) and specialized applications (impulsive control)
- Bridges classical rotor dynamics (symmetric systems) with practical nonlinear phenomena
- Foundation for modern condition monitoring and predictive maintenance

**Relationship to Impulse/Discontinuity Framework**:
- **Implicit treatment**: Oil-whirl instability ↔ impulsive bearing forces
- **Not explicit**: Does NOT use delta function or distribution theory
- **Practical emphasis**: Focuses on prediction and control, not mathematical formalism
- **Complementary to**: Duffy (theory), Pleshkov (algorithms), Yang (control applications)

---

**Document created**: August 17, 2026
**Analysis focus**: Rotor-bearing dynamics, oil-whirl instability, nonlinear bearing behavior, modal testing, condition monitoring
