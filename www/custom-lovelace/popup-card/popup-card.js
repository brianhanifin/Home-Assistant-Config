(function (){
const thisScript = document.currentScript;
customElements.whenDefined('card-tools').then(() => {
  cardTools = customElements.get('card-tools');

  document.querySelector("home-assistant").addEventListener("hass-more-info", (e) => {
    const data = Object.assign({},
      cardTools.lovelace.config.popup_cards,
      cardTools.lovelace.config.views[cardTools.lovelace.current_view].popup_cards,
    );
    if(e.detail) {
      cardTools.logger(`Opening more-info dialog for ${e.detail.entityId}`, thisScript);
      cardTools.logger(`Overridden dialogs:`, thisScript);
      cardTools.logger(Object.keys(data), thisScript);
    }
    if(e.detail && e.detail.entityId && data[e.detail.entityId]) {
      let settings = data[e.detail.entityId];
      while(settings && typeof settings === "string") settings = data[settings];
      if(!settings) return;
      const card = cardTools.createCard(settings.card);
      if(cardTools.hass) card.hass = cardTools.hass;
      cardTools.popUp(settings.title, card, settings.large || false);
    }
  });

});
})();
