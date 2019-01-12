class PopupCard extends HTMLElement {

  makeCard(config) {
    let tag = config.type;
    if(tag.startsWith("custom:"))
      tag = tag.substr(7);
    else
      tag = `hui-${tag}-card`;
    let card = document.createElement(tag);
    card.setConfig(config);
    return card;
  }

  setConfig(config) {
    this.style.margin = "0";
    this.config = config;
    this.config.title = this.config.title || this.config.entity;
    document.querySelector("home-assistant").addEventListener("hass-more-info", (e) => this._handleMoreInfo(e));

    if (! Array.isArray(this.config.entity))
    {
      this.config.entity = [this.config.entity];
    }

    this.card = this.makeCard(config.card);
    this.header = document.createElement('div');
    this.header.innerHTML = `
    <style>
      app-toolbar {
        color: var(--more-info-header-color);
        background-color: var(--more-info-header-background);
      }
    </style>
    <app-toolbar>
      <paper-icon-button
        icon="hass:close"
        dialog-dismiss=""
      ></paper-icon-button>
      <div class="main-title" main-title="">
        ${this.config.title}
      </div>
    </app-toolbar>
    `;
  }

  _handleMoreInfo(e) {
    if(this.card.parentNode) {
      this.header.parentNode.removeChild(this.header);
      this.card.parentNode.removeChild(this.card);
    }
    if(e.detail && e.detail.entityId && this.offsetWidth && this.config.entity.includes(e.detail.entityId)) {
      let moreInfo = document.querySelector("home-assistant").__moreInfoEl;
      moreInfo.style.overflowY = 'auto';
      moreInfo._page = "none";
      moreInfo.shadowRoot.appendChild(this.header);
      moreInfo.shadowRoot.appendChild(this.card);
    }
  }

  set hass(hass) {
    if(this.card)
      this.card.hass = hass;
  }

  getCardSize() {
    return 0;
  }

}

customElements.define("popup-card", PopupCard);