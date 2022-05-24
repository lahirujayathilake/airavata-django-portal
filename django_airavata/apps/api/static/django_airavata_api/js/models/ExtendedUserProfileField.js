import BaseModel from "./BaseModel";
import ExtendedUserProfileFieldChoice from "./ExtendedUserProfileFieldChoice";
import ExtendedUserProfileFieldLink from "./ExtendedUserProfileFieldLink";

const FIELDS = [
  "id",
  "name",
  "help_text",
  "order",
  {
    name: "created_date",
    type: "date",
  },
  {
    name: "updated_date",
    type: "date",
  },
  "field_type",
  {
    name: "links",
    list: true,
    type: ExtendedUserProfileFieldLink,
  },
  // For user_agreement type
  "checkbox_label",
  // For single_choice and multi_choice types
  {
    name: "choices",
    list: true,
    type: ExtendedUserProfileFieldChoice,
  },
  "other",
  "required",
];

export default class ExtendedUserProfileField extends BaseModel {
  constructor(data = {}) {
    super(FIELDS, data);
  }
  toJSON() {
    const copy = Object.assign({}, this);
    // Remove unnecessary properties
    switch (this.field_type) {
      case "text":
        delete copy["other"];
        delete copy["choices"];
        delete copy["checkbox_label"];
        break;
      case "single_choice":
      case "multi_choice":
        delete copy["checkbox_label"];
        break;
      case "user_agreement":
        delete copy["other"];
        delete copy["choices"];
        break;
      default:
        // eslint-disable-next-line no-console
        console.error("Unrecognized field type", this.field_type);
        break;
    }
    return copy;
  }
}
