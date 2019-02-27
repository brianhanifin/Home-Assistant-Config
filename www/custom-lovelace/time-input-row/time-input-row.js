class TimeInputRow extends Polymer.Element {

  static get template() {
    return Polymer.html`
    <hui-generic-entity-row hass="[[_hass]]" config="[[_config]]">
      <paper-time-input hour="[[hour]]" min="[[minute]]" on-change="valueChanged" id="input" hide-label="true" format="24"></paper-time-input>
      </hui-generic-entity-row>
    `
  }

  ready() {
    super.ready();
    this.$.input.addEventListener('click', ev => ev.stopPropagation());
  }

  setConfig(config) {
    this._config = config;
  }

  valueChanged(ev) {
    const time = this.$.input.value.replace(/^\s+|\s+$/g,'');
    const param = {
      entity_id: this._config.entity,
      time: `${time}:00`,
    };
    this._hass.callService('input_datetime', 'set_datetime', param);
  }

  set hass(hass) {
    this._hass = hass;
    let stateObj = hass.states[this._config.entity];
    if(stateObj) {
      this.hour = stateObj.attributes.hour;
      this.minute = stateObj.attributes.minute;
    }
  }
}

customElements.define('time-input-row', TimeInputRow);
