# Web Artifacts Pyl.Tech — Référence

Pour artifacts HTML, React, dashboards, mockups, landing pages au look **officiel** Pyl.Tech.

## Variables CSS racine

À placer dans `:root` au début de tout artifact :

```css
:root {
  /* Couleurs de base (text et arrière-plans) */
  --pyl-navy-dark: #0b132b;       /* Titles color / Dark background */
  --pyl-white: #ffffff;           /* Slides background */
  --pyl-body-grey: #4f4f4f;       /* Body text color */
  --pyl-grey-bg: #eeeeee;         /* Shape / grey slide background */
  
  /* Accentuation */
  --pyl-yellow: #F4BF46;          /* Primary (Accentuation 1) */
  --pyl-navy: #0d2149;            /* Accentuation 2 */
  --pyl-blue-teal: #208AAE;       /* Accentuation 3 */
  --pyl-teal: #5BC0BE;            /* Accentuation 4 */
  
  /* Sémantique */
  --pyl-success: #138636;         /* Accentuation 5 */
  --pyl-danger: #C91432;          /* Accentuation 6 */
  
  /* Partenaire */
  --pyl-intelcia: #E91E63;
  
  /* Typographie */
  --pyl-font-sans: 'Poppins', 'Inter', 'Montserrat', system-ui, -apple-system, sans-serif;
  
  /* Rayons (la charte est plutôt droite) */
  --pyl-radius-sm: 2px;
  --pyl-radius-md: 4px;
  --pyl-radius-lg: 8px;
  
  /* Ombres (très subtiles, style flat) */
  --pyl-shadow-sm: 0 1px 2px rgba(11, 19, 43, 0.04);
  --pyl-shadow-md: 0 1px 3px rgba(11, 19, 43, 0.06);
}
```

## Import de la police Poppins

En haut du HTML :

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
```

Puis dans CSS :

```css
body {
  font-family: var(--pyl-font-sans);
  color: var(--pyl-body-grey);   /* #4f4f4f — pas navy ! */
  background: var(--pyl-white);
  font-size: 12pt;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

h1, h2, h3, h4 {
  color: var(--pyl-navy-dark);  /* #0b132b — titres uniquement */
  font-weight: 700;
}
```

## Composants de base

### Header de page (cartouche numéroté + titre + traits)

```html
<header class="pyl-page-header">
  <hr class="pyl-divider pyl-divider--top" />
  <div class="pyl-header-row">
    <div class="pyl-section-badge">02</div>
    <div class="pyl-header-text">
      <h1>Analyse de vos usages</h1>
      <p class="pyl-subtitle">Une macro-analyse révélant un fort potentiel.</p>
    </div>
  </div>
  <hr class="pyl-divider pyl-divider--bottom" />
</header>
```

```css
.pyl-page-header {
  padding: 0 32px;
  margin-bottom: 24px;
}
.pyl-divider {
  border: none;
  border-top: 1px solid var(--pyl-navy-dark);
  margin: 0;
}
.pyl-header-row {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  padding: 16px 0;
}
.pyl-section-badge {
  background: var(--pyl-yellow);
  color: var(--pyl-white);
  font-weight: 700;
  font-size: 18px;
  width: 56px;
  height: 56px;
  display: grid;
  place-items: center;
  border-radius: var(--pyl-radius-sm);
  flex-shrink: 0;
}
.pyl-header-text h1 {
  font-size: 28px;
  font-weight: 700;
  color: var(--pyl-navy-dark);
  margin: 0 0 4px;
  line-height: 1.2;
}
.pyl-subtitle {
  font-size: 14px;
  color: var(--pyl-body-grey);
  margin: 0;
  font-weight: 400;
}
```

### Card avec header coloré

```html
<div class="pyl-card pyl-card--navy">
  <div class="pyl-card-header">
    <span class="pyl-card-icon" aria-hidden="true">📋</span>
    <h3>Processus ITSM &amp; Qualification</h3>
  </div>
  <ul class="pyl-bullets">
    <li><strong>Confusion Incident/RFC</strong> : près de 15 % des tickets sont mal classés.</li>
    <li><strong>Gestion des priorités</strong> : usage non standard du niveau "Bloqueur".</li>
  </ul>
</div>
```

```css
.pyl-card {
  background: var(--pyl-white);
  border-radius: var(--pyl-radius-md);
  box-shadow: var(--pyl-shadow-md);
  padding: 24px;
  border-top: 6px solid var(--pyl-navy);
  display: flex;
  flex-direction: column;
  gap: 12px;
  border: 1px solid var(--pyl-grey-bg);
}
.pyl-card--navy { border-top-color: var(--pyl-navy); }
.pyl-card--blue-teal { border-top-color: var(--pyl-blue-teal); }
.pyl-card--teal { border-top-color: var(--pyl-teal); }
.pyl-card--yellow { border-top-color: var(--pyl-yellow); }

.pyl-card-header {
  display: flex;
  align-items: center;
  gap: 10px;
}
.pyl-card-header h3 {
  font-size: 18px;
  font-weight: 700;
  color: var(--pyl-navy);
  margin: 0;
}
.pyl-card--blue-teal .pyl-card-header h3 { color: var(--pyl-blue-teal); }
.pyl-card--teal .pyl-card-header h3 { color: var(--pyl-teal); }

/* Bullets carrés jaunes (charte officielle) */
.pyl-bullets {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.pyl-bullets li {
  position: relative;
  padding-left: 18px;
  font-size: 12pt;
  color: var(--pyl-body-grey);
  line-height: 1.5;
}
.pyl-bullets li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 8px;
  width: 8px;
  height: 8px;
  background: var(--pyl-yellow);  /* jaune charte */
  border-radius: 0;
}
```

### Surlignage jaune (highlight style "marqueur fluo")

Pour mettre en avant un mot ou une phrase à la manière de la charte officielle :

```html
<p>
  Notre <span class="pyl-highlight">expertise Workspace</span> couvre l'ensemble
  des besoins du <span class="pyl-highlight">Mouvement E.Leclerc</span>.
</p>
```

```css
.pyl-highlight {
  background: var(--pyl-yellow);
  color: var(--pyl-navy-dark);
  padding: 0 4px;
  font-weight: 600;
}
```

### Badge triangulaire NEW / UPDATED

```html
<div class="pyl-card pyl-card--new">
  <span class="pyl-corner-badge">NEW</span>
  ...
</div>
```

```css
.pyl-card { position: relative; overflow: hidden; }

.pyl-corner-badge {
  position: absolute;
  top: 0;
  left: 0;
  width: 60px;
  height: 60px;
  /* triangle navy */
  background: linear-gradient(135deg, var(--pyl-navy-dark) 0%, var(--pyl-navy-dark) 50%, transparent 50%);
  /* Note: c'est l'exception aux "pas de gradient" — c'est un triangle plat, le gradient n'est qu'un trick CSS */
  color: var(--pyl-white);
  font-size: 9px;
  font-weight: 700;
  text-align: center;
  transform: rotate(0deg);
}
.pyl-corner-badge::before {
  content: 'NEW';
  position: absolute;
  top: 10px;
  left: 4px;
  transform: rotate(-45deg);
}
```

### KPI géant

```html
<div class="pyl-kpi">
  <span class="pyl-kpi-number">75 %</span>
  <span class="pyl-kpi-label">de demandes de service</span>
  <span class="pyl-kpi-sublabel">et seulement 20 % d'incidents</span>
</div>
```

```css
.pyl-kpi {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.pyl-kpi-number {
  font-size: 56px;
  font-weight: 700;
  color: var(--pyl-blue-teal);  /* turquoise officiel */
  line-height: 1;
}
.pyl-kpi-label {
  font-size: 16px;
  font-weight: 600;
  color: var(--pyl-navy-dark);
}
.pyl-kpi-sublabel {
  font-size: 13px;
  color: var(--pyl-body-grey);
}
```

### Bouton "primary" Pyl.Tech

```css
.pyl-btn {
  background: var(--pyl-yellow);
  color: var(--pyl-navy-dark);
  font-weight: 600;
  font-size: 14px;
  padding: 10px 20px;
  border: none;
  border-radius: var(--pyl-radius-md);
  cursor: pointer;
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.pyl-btn:hover {
  transform: translateY(-1px);
  box-shadow: var(--pyl-shadow-md);
}
.pyl-btn--secondary {
  background: transparent;
  color: var(--pyl-navy-dark);
  border: 1.5px solid var(--pyl-navy-dark);
}
.pyl-btn--success {
  background: var(--pyl-success);
  color: var(--pyl-white);
}
.pyl-btn--danger {
  background: var(--pyl-danger);
  color: var(--pyl-white);
}
```

### Tableau

```css
.pyl-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 10pt;  /* taille officielle tableaux */
}
.pyl-table thead {
  background: var(--pyl-navy-dark);
}
.pyl-table th {
  text-align: left;
  padding: 12px 16px;
  font-weight: 700;
  color: var(--pyl-white);
  font-size: 11pt;
}
.pyl-table tbody tr:nth-child(odd) {
  background: var(--pyl-navy);
  color: var(--pyl-white);
}
.pyl-table tbody tr:nth-child(even) {
  background: var(--pyl-white);
  color: var(--pyl-body-grey);
}
.pyl-table td {
  padding: 10px 16px;
}
```

### Footer copyright

```html
<footer class="pyl-footer">
  <span>© Copyright 2026 Pyl.Tech</span>
  <span>34</span>
</footer>
```

```css
.pyl-footer {
  position: absolute;
  bottom: 16px;
  left: 32px;
  right: 32px;
  display: flex;
  justify-content: space-between;
  font-size: 9pt;
  color: var(--pyl-blue-teal);  /* turquoise officiel */
}
```

## Tokens pour projet React + Tailwind

```jsx
// Couleurs custom officielles Pyl.Tech
const PYL = {
  navyDark: '#0b132b',
  white: '#ffffff',
  bodyGrey: '#4f4f4f',
  greyBg: '#eeeeee',
  yellow: '#F4BF46',
  navy: '#0d2149',
  blueTeal: '#208AAE',
  teal: '#5BC0BE',
  success: '#138636',
  danger: '#C91432',
};
```

Dans le JSX, utiliser les arbitrary values Tailwind :

```jsx
<div className="bg-[#F4BF46] text-[#0b132b] p-6">
  <h2 className="text-2xl font-bold">Titre Pyl.Tech</h2>
  <p className="text-[#4f4f4f]">Corps de texte officiel</p>
</div>
```

## Composant React réutilisable (exemple)

```jsx
function PylCard({ accent = 'navy', icon, title, children }) {
  const accentColors = {
    navy: '#0d2149',
    blueTeal: '#208AAE',
    teal: '#5BC0BE',
    yellow: '#F4BF46',
  };
  const accentColor = accentColors[accent] || accentColors.navy;
  // Si le header est jaune, le titre reste navy pour la lisibilité
  const titleColor = accent === 'yellow' ? '#0b132b' : accentColor;
  
  return (
    <div
      className="bg-white p-6 flex flex-col gap-3 border border-[#eeeeee]"
      style={{ borderTop: `6px solid ${accentColor}`, borderRadius: '4px' }}
    >
      <div className="flex items-center gap-2">
        {icon && <span className="text-lg" aria-hidden="true">{icon}</span>}
        <h3 className="text-lg font-bold" style={{ color: titleColor }}>
          {title}
        </h3>
      </div>
      <div className="text-sm leading-relaxed" style={{ color: '#4f4f4f' }}>
        {children}
      </div>
    </div>
  );
}

function PylHighlight({ children }) {
  return (
    <span style={{
      background: '#F4BF46',
      color: '#0b132b',
      padding: '0 4px',
      fontWeight: 600,
    }}>
      {children}
    </span>
  );
}
```

## Layout type "page Pyl.Tech"

Pour reproduire fidèlement une slide en HTML (ex: dashboard, page de rapport interactif) :

```html
<div class="pyl-page">
  <div class="pyl-page-top-right-logo">Pyl.Tech</div>
  
  <header class="pyl-page-header">
    <hr class="pyl-divider" />
    <div class="pyl-header-row">
      <div class="pyl-section-badge">02</div>
      <div class="pyl-header-text">
        <h1>Titre de la page</h1>
        <p class="pyl-subtitle">Sous-titre descriptif</p>
      </div>
    </div>
    <hr class="pyl-divider" />
  </header>
  
  <main class="pyl-content">
    <!-- Cards, graphiques, tableaux ici -->
  </main>
  
  <footer class="pyl-footer">
    <span>© Copyright 2026 Pyl.Tech</span>
    <span>1</span>
  </footer>
</div>
```

```css
.pyl-page {
  position: relative;
  width: 1280px;
  min-height: 720px;
  background: var(--pyl-white);
  padding: 16px 0 48px;
  font-family: var(--pyl-font-sans);
}
.pyl-page-top-right-logo {
  position: absolute;
  top: 20px;
  right: 32px;
  font-weight: 700;
  color: var(--pyl-navy-dark);
}
.pyl-content {
  padding: 0 32px;
}
```

## À toujours faire dans un artifact Pyl.Tech

- Footer copyright "© Copyright [année] Pyl.Tech" en bas en **turquoise** `#208AAE`
- Logo "Pyl.Tech" en haut à droite (sauf si page de couverture)
- Cartouche jaune avec numéro de section quand applicable
- Titre encadré entre 2 traits horizontaux fins navy
- Police Poppins importée
- Variables CSS dans `:root`
- **Texte courant en gris `#4f4f4f`**, jamais en navy
- Bullets carrés jaunes
- Pas de couleurs hors palette officielle

## À ne jamais faire

- Texte courant en navy (la charte impose `#4f4f4f` gris)
- Utiliser localStorage / sessionStorage (interdit dans les artifacts Claude.ai)
- Empiler 4+ couleurs principales sur une même page
- Texte jaune sur fond blanc (contraste insuffisant)
- Texte navy sur fond navy
- Coins très arrondis (la charte est plutôt droite, max 4-8 px)
- Animations excessives
- Ombres portées marquées (la charte est très flat)
