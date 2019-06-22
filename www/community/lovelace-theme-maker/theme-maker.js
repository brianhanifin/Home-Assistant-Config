customElements.whenDefined('card-tools').then(() => {
class ThemeMaker extends cardTools.LitElement {

  setConfig(config) {
    this._config = config
    this.colorPickerColor = {
      h: 25,
      s: 10,
    };
    this.color = "";
    this.theme = {};
    this.name = "new_theme";
  }

  static get styles() {
    return cardTools.LitCSS`
    ha-card {
      padding: 16px;
    }
    .side-by-side {
      display: flex;
    }
    `;
  }

  render() {
    return cardTools.LitHtml`
    <ha-card header="Theme Maker">
    <div id="classes">
    ${
      Object.keys(this.theme).map((style, index) => {
        return cardTools.LitHtml`
        <div class="side-by-side">
          <paper-input
            label="Variable"
            .value="${style}"
            .configValue="PRP:${style}"
            @change="${this.styleChanged}"
          ></paper-input>
          <paper-input
            label="Value"
            .value="${this.theme[style]}"
            .configValue="VAL:${style}"
            id="VAL-${style}"
            @change="${this.styleChanged}"
          ></paper-input>
          </div>
        `;
      })
    }
    <div class="side-by-side">
      <paper-input
        label="New"
        .value=" "
        .configValue="${'NEW'}"
        @change="${this.styleChanged}"
      ></paper-input>
      <paper-input
        label="Value"
        disabled="true"
      ></paper-input>
      </div>
    </div>
    <mwc-button
    @click="${this.yamlMode}"
    >Import/Export</mwc-button>
    </ha-card>
    `;
  }

  updateStyles() {
    document.querySelector("html").removeAttribute("style");
    Object.keys(this.theme).forEach((style) => {
      document.querySelector("html").style.setProperty("--"+style, this.theme[style]);
    });
  }

  styleChanged(ev) {
    let cmd = ev.target.configValue.substr(0,3);
    let property = ev.target.configValue.substr(4);
    let value = ev.target.value;

    if(cmd === "NEW") {
      property = value;
      value = "";
      ev.target.value = "";
    }
    if (cmd === "PRP") {
      let oldprop = property;
      property = value;
      value = this.theme[oldprop];
      delete this.theme[oldprop];
    }

    if(property)
      this.theme[property] = value;

    this.updateStyles();
    this.requestUpdate();

    if(cmd === "NEW")
      this.updateComplete.then(() => {
        this.shadowRoot.querySelector("ha-card #classes div #VAL-" + property).focus();
      });
  }

  importTheme(yaml) {
    const lines = yaml.split('\n');

    this.name = lines[0].trim().substr(0,lines[0].trim().length - 1) || "new_theme";

    this.theme = {}
    for(var i = 1; i < lines.length; i++) {
      var line = lines[i];
      // Remove comments (Anything after # unless the # is within quotes)
      line = line.replace(/"[^"]*"|'[^']*'|(#.*)/g, (m, g1) => {
        if(g1) return '';
        return m;
      });
      if(!line.includes(":")) continue;
      const property = line.split(":")[0].trim();
      const value = line.split(/:(.+)/)[1].trim().replace(/^['"]|['"]$/g,'');
      this.theme[property] = value;
    }
    this.updateStyles();
    this.requestUpdate();
  }

  exportTheme() {
    let exp = this.name + ":"
    Object.keys(this.theme).forEach((style) => {
      if(this.theme[style].includes('"'))
        exp += `\n  ${style}: '${this.theme[style]}'`;
      else
        exp += `\n  ${style}: "${this.theme[style]}"`;
    });
    return exp;
  }

  yamlMode(ev) {
    const card = document.createElement("ha-card");
    card.style.setProperty("padding", "16px");
    card.innerHTML = `
    <textarea
      style="width:100%; height: 300px; resize: none;"
      ></textarea>
      <mwc-button>
      Load
      </mwc-button>
    `;
    card.querySelector("mwc-button").onclick = () => {this.importTheme(card.querySelector("textarea").value); cardTools.closePopUp();};
    card.querySelector("textarea").value = this.exportTheme();
    cardTools.popUp("Theme", card, true);
  }

}
customElements.define('theme-maker', ThemeMaker);
});

window.setTimeout(() => {
  if(customElements.get('card-tools')) return;
  customElements.define('theme-maker', class extends HTMLElement{
    setConfig() { throw new Error("Can't find card-tools. See https://github.com/thomasloven/lovelace-card-tools");}
  });
}, 2000);
