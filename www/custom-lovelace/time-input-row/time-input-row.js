customElements.whenDefined('card-tools').then(() => {
let cardTools = customElements.get('card-tools');
class TimeInputRow extends cardTools.LitElement {

  static get properties() {
    return {
      stateObj: Object,
    };
  }

  static get styles() {
    return cardTools.LitCSS`
    :host {
      --paper-input-container-shared-input-style_-_-webkit-appearance: textfield;
      --paper-input-container-shared-input-style_-_-moz-appearance: textfield;
      --paper-input-container-shared-input-style_-_appearance: textfield;
    }
    .time-input-wrap {
      display: flex;
      flex-direction: row;
    }
    paper-input {
      text-align: center;
    }
    `;
  }

  render() {
    const year = cardTools.LitHtml`
      <paper-input
      id="year"
      type="number"
      no-label-float=""
      maxlength="4"
      max="9999"
      min="0"
      auto-validate="true"
      value="${this.getYear()}"
      style="width: 50px;"
      @click="${(ev) => ev.stopPropagation()}"
      @change="${this.valueChanged}"
      >
      <span suffix slot="suffix">
        ${this.iso ? `-` : ``}
      </span>
      </paper-input>
    `;
    const month = cardTools.LitHtml`
      <paper-input
      id="month"
      type="number"
      no-label-float=""
      maxlength="4"
      max="12"
      min="01"
      auto-validate="true"
      value="${this.getMonth()}"
      style="width: 30px;"
      @click="${(ev) => ev.stopPropagation()}"
      @change="${this.valueChanged}"
      >
      <span suffix slot="suffix">
        ${this.iso ? `-` : `/`}
      </span>
      </paper-input>
    `;
    const day = cardTools.LitHtml`
      <paper-input
      id="day"
      type="number"
      no-label-float=""
      maxlength="4"
      max="31"
      min="01"
      auto-validate="true"
      value="${this.getDay()}"
      style="width: 30px;"
      @click="${(ev) => ev.stopPropagation()}"
      @change="${this.valueChanged}"
      >
      <span suffix slot="suffix">
        ${this.iso ? `` : `/`}
      </span>
      </paper-input>
    `;

    return cardTools.LitHtml`
    <hui-generic-entity-row
    .hass="${this._hass}"
    .config="${this._config}"
    >
      ${this.stateObj.attributes.has_date === true ?
        cardTools.LitHtml`
        <div class="time-input-wrap">
          ${this.iso ?
            cardTools.LitHtml`${year}${month}${day}` :
            cardTools.LitHtml`${month}${day}${year}`}
        </div>
        ` : ``}

      ${this.stateObj.attributes.has_time === true &&
      this.stateObj.attributes.has_date === true ? `,` : ``}

      ${this.stateObj.attributes.has_time === true ?
      cardTools.LitHtml`
        <paper-time-input
        .hour="${this.getHour()}"
        .min="${this.getMinute()}"
        .amPm="${this.getAMPM()}"
        @change="${this.valueChanged}"
        @click="${(ev) => ev.stopPropagation()}"
        id="time"
        hide-label="true"
        format="${this.iso ? '24' : '12'}"
        ></paper-time-input>
      ` : ``}

    </hui-generic-entity-row>
    `
  }

  firstUpdated() {
    this.active = true;
  }

  setConfig(config) {
    this.active = false
    this._config = config;
    this.iso = !config.silly_format;
  }

  getHour() {
    if(this.stateObj.state === "unknown")
      return "";
    return ("0" + (this.iso ?
      this.stateObj.attributes.hour :
      this.stateObj.attributes.hour%12)
    ).slice(-2);
  }
  getMinute() {
    if(this.stateObj.state === "unknown")
      return "";
    return ("0" + this.stateObj.attributes.minute).slice(-2);
  }
  getYear() {
    if(this.stateObj.state === "unknown")
      return "";
    return this.stateObj.attributes.year;
  }
  getMonth() {
    if(this.stateObj.state === "unknown")
      return "";
    return ("0" + this.stateObj.attributes.month).slice(-2);
  }
  getDay() {
    if(this.stateObj.state === "unknown")
      return "";
    return ("0" + this.stateObj.attributes.day).slice(-2);
  }
  getAMPM() {
    if(this.stateObj.state === "unknown")
      return "";
    return (this.stateObj.attributes.hour < 12) ? "AM" : "PM";
  }

  getDateString() {
    if(this.stateObj.state === "unknown")
      return "";
    return "" +
      this.stateObj.attributes.year +
      "-" +
      ("0" + this.stateObj.attributes.month).slice(-2) +
      "-" +
      ("0" + this.stateObj.attributes.day).slice(-2);
  }

  valueChanged(ev) {
    if(!this.active) return;
    let param = {
      entity_id: this._config.entity,
    };
    if(this.stateObj.attributes.has_time) {
      const timeEl = this.shadowRoot.querySelector("#time");
      param.time = "" +
        (parseInt(timeEl.hour) +
          (!this.iso && timeEl.amPm == "PM" ? 12 : 0)) + ":" +
        timeEl.min + ":00";
    }
    if(this.stateObj.attributes.has_date)
      param.date = "" +
        this.shadowRoot.querySelector("#year").value + "-" +
        this.shadowRoot.querySelector("#month").value + "-" +
        this.shadowRoot.querySelector("#day").value;
    this._hass.callService('input_datetime', 'set_datetime', param);
  }

  set hass(hass) {
    this._hass = hass;
    this.stateObj = hass.states[this._config.entity];
  }
}

customElements.define('time-input-row', TimeInputRow);
});
window.setTimeout(() => {
  if(customElements.get('card-tools')) return;
  customElements.define('time-input-row', class extends HTMLElement{
    setConfig() { throw new Error("Can't find card-tools. See https://github.com/thomasloven/lovelace-card-tools");}
  });
}, 2000);
